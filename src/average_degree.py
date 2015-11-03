import settings, os, re, itertools, json
from datetime import datetime, timedelta
from collections import deque

class Tweet:
    def __init__(self, text):
        self.text = text
        self.timestamp = 0
        tweet_dict = json.loads(text)
        self.hashtags = []
        for data in tweet_dict['entities']['hashtags']:
            self.hashtags.append(data['text'].lstrip('#'))
        matches = re.search('\w{3}\s\w{3}\s\d{1,2}\s(\d{1,2}:\d{2}:\d{2})\s[+-]\d{1,4}\s\d{4}', self.text)
        if matches:
            self.timestamp = datetime.strptime(matches.group(1), '%H:%M:%S')
        else:
            print "Tweet failed to parse: {}".format(self.text)


    def get_timestamp(self):
        return self.timestamp

    def get_hashtags(self):
        return self.hashtags

    def get_hashtag_combinations(self):
        return itertools.combinations(self.hashtags, 2)

class Graph:
    def __init__(self):
        self.graph = {}

    def add_double_edge(self, edge):
        self.graph.setdefault(edge[0], {})
        self.graph[edge[0]].setdefault(edge[1], 0)
        self.graph[edge[0]][edge[1]] += 1
        self.graph.setdefault(edge[1], {})
        self.graph[edge[1]].setdefault(edge[0], 0)
        self.graph[edge[1]][edge[0]] += 1

    def link_hashtags(self, tweet):
        for edge in tweet.get_hashtag_combinations():
            self.add_double_edge(edge)

    def remove_edge(self, edge):
        if edge[0] in self.graph[edge[1]]:
            self.graph[edge[1]][edge[0]] -= 1
            if self.graph[edge[1]][edge[0]] < 1:
                del self.graph[edge[1]][edge[0]]
        if edge[1] in self.graph[edge[0]]:
            self.graph[edge[0]][edge[1]] -= 1
            if self.graph[edge[0]][edge[1]] < 1:
                del self.graph[edge[0]][edge[1]]

    def unlink_hashtags(self, tweet):
        for edge in tweet.get_hashtag_combinations():
            self.remove_edge(edge)

    def average_degree(self):
        sum_degree = 0
        sum_vertices = 0
        for vertex, edge_dict in self.graph.iteritems():
            sum_degree += len(edge_dict)
            if len(edge_dict):
                sum_vertices += 1
        return float(sum_degree)/sum_vertices

with open(os.path.join(settings.INPUT_DIR, 'tweets.txt')) as input_file:
    window = deque()
    graph = Graph()
    for start_index, line in enumerate(input_file):
        tweet = Tweet(line)
        end_time = tweet.get_timestamp()
        start_time = end_time - timedelta(0, 60)
        graph.link_hashtags(tweet)
        window.append(tweet)
        while window[0].get_timestamp() < start_time:
            old_tweet = window.popleft()
            graph.unlink_hashtags(old_tweet)
        print graph.average_degree()
