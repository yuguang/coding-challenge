# example of program that calculates the number of tweets cleaned
import settings, os, json
num_cleaned = 0
output_lines = []

def encode_ascii(input):
    output_chars = []
    for character in input:
        if ord(character) < 128:
            output_chars.append(character)
    return ''.join(output_chars)

with open(os.path.join(settings.INPUT_DIR, 'tweets.txt')) as input_file:
    for tweet in input_file:
        tweet_dict = json.loads(tweet)
        cleaned_text = encode_ascii(tweet_dict['text'])
        output_lines.append('{} (timestamp: {})'.format(cleaned_text, tweet_dict['created_at']))
        if len(cleaned_text) != len(tweet_dict['text']):
            num_cleaned += 1

print(output_lines)
print(num_cleaned)
