# Twitter-Sentiment-Analysis
Analysis and Modelling of Sentiments based on Tweets


EXTRACT ALL TWEETS

./code/data_mining/extract_tweets.py

TOKENIZE


./code/data_mining/ark-tweet-nlp/runTagger.sh ./dataset/tweets_training.txt > ./dataset/tweets_training_tokenized.txt
./code/data_mining/ark-tweet-nlp/runTagger.sh ./dataset/tweets_testing.txt > ./dataset/tweets_training_testing.txt


GENERATE FINAL INPUT

./code/data_mining/final_input_generator.py

