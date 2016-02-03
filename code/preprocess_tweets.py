import re

spChar=' \r\t\n/.,\';\\][|":}{`=_)(&^%@#0987654321'

#spTagList=['#','U','@',',','E','~','$','G']

def replacing_emoticons(tweet, token, emoticon_dict):

    for i in xrange(len(tweet)):
        if tweet[i] in emoticon_dict:
            tweet[i] = emoticon_dict[tweet[i]]
            token[i] = 'E'

    return tweet, token

def removingNonEnglish(tweet, token):

    Tweet, Token = [], []
    for i in xrange(len(tweet)):
        if tweet[i]!='':
            c=re.match(r'([a-zA-z0-9 \+\?\.\*\^\$\(\)\[\]\{\}\|\\/:;\'\"><,.#@!~`%&-_=])+$',tweet[i])
            if c:
                Tweet.append(tweet[i])
                Token.append(token[i])
    return Tweet, Token

def removeNumbers_noun_prepositions(tweet, token):

    Tweet, Token = [], []
    for i in xrange(len(tweet)):
        if token[i]!='$' and token[i]!='^' and token[i]!='Z' and token[i]!='O' and token[i]!='P':
            Tweet.append(tweet[i])
            Token.append(token[i])
    return Tweet, Token

def acronym_expansion(tweet, token, acro_dict):

    Tweet, Token, cnt = [], [], 0
    for i in xrange(len(tweet)):
        word=tweet[i].lower().strip(spChar)
        if word:
            if word in acro_dict:
                cnt+=1
                Tweet.extend(acro_dict[word][0])
                Token.extend(acro_dict[word][1])
            else:
                Tweet.append(tweet[i])
                Token.append(token[i])
    return Tweet, Token, cnt

def replace_repetition(tweet):
    cnt=0
    for i in xrange(len(tweet)):
        l=list(tweet[i])
        if len(l) > 3:
            f=0
            for j in range(3, len(l)):
                if l[j-3].lower()==l[j-2].lower()==l[j-1].lower()==l[j].lower():
                    l[j-3]=''

                    if f==0:
                        cnt+=1
                        f=1
            tweet[i]=''.join(l).strip(spChar)

    return tweet, cnt

def replace_hash(tweet, token):
    for i in xrange(len(tweet)):
        if token[i]=='#' or tweet[i].startswith('#'):
            token[i]='#'
            tweet[i]=tweet[i][1:].strip(spChar)
    return tweet, token

def remove_url_and_target(tweet, token):

    Token, Tweet =[], []
    for i in xrange(len(tweet)):
        if token[i]=='U' or token[i]=='@' or tweet[i].startswith('@'):
            continue
        else:
            Tweet.append(tweet[i])
            Token.append(token[i])
    return Tweet, Token

def expansion_negation(tweet, token):
    Tweet, Token = [], []
    for i in xrange(len(tweet)):
        word=tweet[i].lower().strip(spChar)
        if(word[-3:]=="n't"):
            if(word[-5:]=="can't"):
                Tweet.append('can')
            else:
                Tweet.append(word[:-3])
            Tweet.append('not')
            Token.append('V')
            Token.append('R')
        else:
            Tweet.append(tweet[i])
            Token.append(token[i])
    return Tweet, Token

def replace_negation(tweet):
    for i in xrange(len(tweet)):
        word=tweet[i].lower().strip(spChar)
        if(word=="no" or word=="not" or word.count("n't")>0):
            tweet[i]='negation'

    return tweet

def remove_stopwords(tweet, token, stopwords):
    Tweet, Token = [], []
    for i in xrange(len(tweet)):
        if tweet[i].lower().strip(spChar) not in stopwords.keys():
            Tweet.append(tweet[i])
            Token.append(token[i])

    return Tweet, Token


def preprocess(tweet, token , emoticon_dict, acro_dict, stopwords):
    tweet, token = replacing_emoticons(tweet, token, emoticon_dict)
    tweet, token = removingNonEnglish(tweet, token)
    tweet, token = removeNumbers_noun_prepositions(tweet, token)
    tweet, token , cnt1 = acronym_expansion(tweet, token, acro_dict)
    tweet, cnt2 = replace_repetition(tweet)
    tweet, token = replace_hash(tweet, token)
    tweet, token = remove_url_and_target(tweet, token)
    tweet, token = expansion_negation(tweet, token)
    tweet = replace_negation(tweet)
    tweet, token = remove_stopwords(tweet, token, stopwords)

    return tweet, token, cnt1, cnt2
