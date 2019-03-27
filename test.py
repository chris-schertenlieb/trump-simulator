from io import *
from textgenrnn import textgenrnn

# this code is for taking tweets out of a
# file (tweets.txt in this example) and splitting
# them on a delimiter if necessary (\) and
# then pastes them into a new file 'newTweets.txt'
'''tweetList = []
with open('tweets.txt', 'r', errors='replace') as f:
    for line in f:
        #print(line.encode("utf-8"))

        #newLine = line.encode('utf-8')
        #print(newLine)
        newLine = line.split('\\')
        if(len(newLine) > 1):
            tweetList.append(newLine[1])

with open('newTweets.txt', 'w') as f:
    for tweet in tweetList:
        f.write("%s\n" % tweet)'''

# actual code that runs the thingy

textgen = textgenrnn()
textgen.train_from_file('newTweets.txt', num_epochs=1)
textgen.generate()

