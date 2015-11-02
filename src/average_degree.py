import settings, os, re, linecache
from datetime import datetime, timedelta

class Tweet:
    def __init__(self, text):
        self.text = text
        self.timestamp = 0
        self.hashtags = []
        matches = re.search('.*\s\(timestamp:\s\w{3}\s\w{3}\s\d{1,2}\s(\d{1,2}:\d{2}:\d{2})\s[+-]\d{1,4}\s\d{4}\)', self.text)
        if matches:
            self.timestamp = datetime.strptime(matches.group(1), '%H:%M:%S')
        else:
            print "Tweet failed to parse: {}".format(tweet)


    def get_timestamp(self):
        return self.timestamp

with open(os.path.join(settings.INPUT_DIR, 'parsed_tweets.txt')) as input_file:
    # scan through the list
    start = None
    start_line = 0
    for line_index, line in enumerate(input_file):
        tweet = Tweet(line)
        # if the starting timestamp is not set, get it from the current tweet
        if not start:
            start = tweet.get_timestamp()
            start_line = line_index
        # the ending timestamp is 60s + the starting timestamp
        end = start + timedelta(0, 60)
        # continue scanning until the 60s boundary is exceeded
        if tweet.get_timestamp() > end:
            # print out the average degree
        # set starting timestamp to the time after the first tweet in the current set
        start_tweet = Tweet(linecache.getline('parsed', start_line))
        start = start_tweet.get_timestamp()
        start_line = start_line + 1