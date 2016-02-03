spChar=' \r\t\n/.,\';\\][|":}{`=_)(&^%@#0987654321'
stopwords={}

f=open('../dataset/stop_words.txt','r')

for i in f:
        i=i.strip(spChar).lower()
        stopwords[i]=1

f.close()
