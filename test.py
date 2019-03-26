from io import *

#lines = [line.rstrip('\n') for line in open('test.txt', 'w')]
#print (lines)

with open('trump_tweets.txt', 'r', encoding='utf-8', errors='replace') as f:
    for line in f:
        print(line.encode("utf-8"))

