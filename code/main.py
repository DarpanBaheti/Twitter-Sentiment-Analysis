from emoticons_dict import *
from acronym_dict import *
from stop_words_dict import *
from extract_features import *
from svmutil import *

def svm_classify(training_label,training_vector, testing_label, testing_vector):
    
    model= svm_train(training_label,training_vector)
    svm_save_model('svm_anal.model', model)

    label, acc , val = svm_predict(testing_label, testing_vector, model)

    return acc[0]


training_tweets = '../dataset/tweets_training.txt'
testing_tweets = '../dataset/tweets_testing.txt'

training_final_input = '../dataset/final_training_input.txt'
testing_final_input = '../dataset/final_testing_input.txt'

polarity_map={'positive':1,'negative':2,'neutral':3}


d={'positive':1.0,'negative':2.0,'neutral':3.0}


if __name__ == '__main__':
         
    f = open(training_final_input,'r')

    training_label, training_vector = [], []

    for i in f:
        i=i.split('\t')
        label = i[0].strip()
        tweet = i[1].split()
        token = i[2].strip().split()

        training_vector.append(extract_features(tweet, token, stopwords, acro_dict, emoticon_dict))

        training_label.append(d[label])
        
    f = open(testing_final_input,'r')

    testing_label=[]
    testing_vector = []

    for i in f:
        i=i.split('\t')
        label = i[0].strip()
        tweet = i[1].split()
        token = i[2].strip().split()

        testing_vector.append(extract_features(tweet, token, stopwords, acro_dict, emoticon_dict))

        testing_label.append(d[label])
    
    acc = svm_classify(training_label,training_vector, testing_label, testing_vector)

    print "Accuracy:"
    print acc

