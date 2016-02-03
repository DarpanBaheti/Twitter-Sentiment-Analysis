from preprocess_tweets import *

def count_capitals(tweet, token):
    cnt, cap, isCap, percap =0,0,0,0.0

    for i in xrange(len(tweet)):
        if token[i]!='$':
            word = tweet[i].strip(spChar)
            if word:
                cnt+=1
                if word.isupper():
                    cap+=1
    if cap>0:
        isCap = 1
    if cnt >0:
        percap = float(cap)/cnt

    return [percap, isCap]

def count_hastags(tweet, token):

    cnt =0 
    for i in xrange(len(tweet)):
        if token[i]=='#':
            cnt+=1
    return [cnt]

def count_emoticons(tweet, token):
    cnt_pos =0
    cnt_expos =0
    cnt_neg =0
    cnt_exneg =0

    for i in xrange(len(tweet)):
        if token[i]=='E':
            if tweet[i] == 'Extremely-Positive':
                cnt_expos +=1
            elif tweet[i] == 'Positive':
                cnt_pos +=1
            elif tweet[i] == 'Negative':
                cnt_neg +=1
            elif tweet[i] == 'Extremely-Negative':
                cnt_exneg +=1
    return [cnt_pos, cnt_neg, cnt_expos, cnt_exneg]

def count_negation(tweet):
    cnt=0
    for i in xrange(len(tweet)):
        if tweet[i]=='negation':
            cnt+=1
    return [cnt]

def count_spchar(tweet):
    cnt={'*':0,'!':0,'?':0}
    for i in xrange(len(tweet)):
        word=tweet[i].lower().strip(spChar)
        cnt['*']=word.count('*')
        cnt['?']=word.count('?')
        cnt['!']=word.count('!')
            
    return [cnt['?'], cnt['!'], cnt['*']]

def count_postags(tweet, token):
    cnt={'V':0,'P':0,'N':0,'O':0,'A':0,'R':0}

    for i in xrange(len(tweet)):
        word = tweet[i].lower().strip(spChar)

        if token[i] in cnt.keys():
            cnt[token[i]]+=1
    return [cnt['V'], cnt['P'], cnt['N'], cnt['O'], cnt['A'], cnt['R']]

def extract_features(tweet, token, stopwords, acro_dict, emoticon_dict):

    tweet, token, cnt1, cnt2 =  preprocess(tweet, token , emoticon_dict, acro_dict, stopwords)
    
    feature_vector=[]
    feature_vector.extend(count_capitals(tweet, token))
    feature_vector.extend(count_hastags(tweet, token))
    feature_vector.extend(count_emoticons(tweet, token))
    feature_vector.extend(count_negation(tweet))
    feature_vector.extend(count_spchar(tweet))
    feature_vector.extend(count_postags(tweet, token))

    return feature_vector
