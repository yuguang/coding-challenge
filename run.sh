#!/usr/bin/env bash

# example of the run script for running the word count

# I'll execute my programs, with the input directory tweet_input and output the files in the directory tweet_output
chmod +w ./tweet_output/ft1.txt
python3 ./src/words_tweeted.py
python3 ./src/median_unique.py



