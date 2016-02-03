spChar=' \r\t\n/.,\';\\][|":}{`=_)(&^%@#0987654321'
acro_dict={}
f=open('../dataset/acronym_tokenised.txt')
for i in f:

        i=i.split('\t')
        
        word = i[0].split()
        
        if word:
            key = word[0].lower().strip(spChar)

            val=[]
            for k in word[1:]:
                val.append(k.lower().strip(spChar))
        
            token = i[1].split()[1:]

            acro_dict[key]=[val,token]

f.close()

