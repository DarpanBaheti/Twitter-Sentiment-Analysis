f=open('acronym_tokenised.txt','r')
for i in f:
    i=i.split('\t')
    word=i[0].split()
    print word[0]
    print i[1].split()[1:]
    print word[1:]
    break
f.close()
