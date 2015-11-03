# example of program that calculates the number of tweets cleaned
import settings, os, json
num_cleaned = 0

def encode_ascii(input):
    output_chars = []
    for character in input:
        if ord(character) < 128:
            output_chars.append(character)
    return ''.join(output_chars)

with open(os.path.join(settings.INPUT_DIR, 'tweets.txt')) as input_file, open(os.path.join(settings.OUTPUT_DIR, 'ft1.txt'), 'w') as output_file:
    for tweet in input_file:
        tweet_dict = json.loads(tweet)
        cleaned_text = encode_ascii(tweet_dict['text'])
        output_file.write('{} (timestamp: {})\n'.format(cleaned_text, tweet_dict['created_at']))
        if len(cleaned_text) != len(tweet_dict['text']):
            num_cleaned += 1


with open(os.path.join(settings.OUTPUT_DIR, 'ft1.txt'), 'a') as output_file:
    output_file.write('{} tweets contained unicode.'.format(num_cleaned))
