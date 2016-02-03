
# For Training Tweets

f=open('../../dataset/raw_training_data.txt','r')
f1=open('../../dataset/tweets_training.txt','w')

for i in f:
    i=i.split('\t')
    f1.write(i[1])

f.close()
f1.close()


# Testing Tweets

f=open('../../dataset/raw_testing_data.txt','r')
f1=open('../../dataset/tweets_testing.txt','w')

for i in f:
    i=i.split('\t')
    f1.write(i[1])

f.close()
f1.close()
