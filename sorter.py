import os
import ast

files = os.listdir('../tweets')
path = r'sortedTweets'
if not os.path.exists(path):
    os.makedirs(path)
for file in files:
    f = open('../tweets/' + file, 'r')
    data = f.read()
    text = ast.literal_eval(data)
    iphoneCount = 0
    androidCount = 0
    for item in text:
        if 'iPhone' in item['source']:
            title = 'sortedTweets/iphone' + str(iphoneCount)
            tweet = open(title, 'w')
            tweet.write(item['text'])
            tweet.close
            iphoneCount+=1
        elif 'Android' in item['source']:
            title = 'sortedTweets/android' + str(androidCount)
            tweet = open(title, 'w')
            tweet.write(item['text'])
            tweet.close
            androidCount+=1
print('all done')