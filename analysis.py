from __future__ import division
import urllib.request
import csv
from string import punctuation


files = ['negative.txt','positive.txt','obama_tweets.txt']

path='http://www.unc.edu/~ncaren/haphazard/'

for file_name in files:
    
    urllib.request.urlretrieve(path+file_name,file_name)


tweets = open("obama_tweets.txt", 'r').read()
tweets_list = tweets.split('\n')

pos_sent = open("positive.txt", 'r').read()
positive_words = pos_sent.split('\n')
positive_counts = []

neg_sent = open('negative.txt', 'r').read()
negative_words = neg_sent.split('\n')
negative_counts = []


for tweet in tweets_list:
    positive_counter = 0
    negative_counter = 0
    
    tweet_processed = tweet.lower()
    
    
    for p in list(punctuation):
        tweet_processed = tweet_processed.replace(p,'')

    words = tweet_processed.split(' ')
    word_count = len(words)
    for word in words:
        if word in positive_words:
            positive_counter = positive_counter + 1
        elif word in negative_words:
            negative_counter = negative_counter + 1
        
    positive_counts.append(positive_counter/word_count)
    negative_counts.append(negative_counter/word_count)

print(len(positive_counts))

output = zip(tweets_list,positive_counts,negative_counts)


with open('sentiment.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in output:
        writer.writerow(line)