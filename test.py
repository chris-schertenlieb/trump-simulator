from io import *

#lines = [line.rstrip('\n') for line in open('test.txt', 'w')]
#print (lines)

with open('trump_tweets.txt', 'r', errors='replace') as f:
    for line in f:
        #print(line.encode("utf-8"))
        newLine = line.split('|')
        if(len(newLine) > 1):
            print (newLine[1].encode("utf-8"))

