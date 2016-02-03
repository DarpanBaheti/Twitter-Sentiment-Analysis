

emoticon_dict={}

f=open('../dataset/emoticons.txt')
for i in f:

        i=i.split()

        val=i[-1].strip()

        for k in i[:-1]:
            emoticon_dict[k]=val
f.close()
