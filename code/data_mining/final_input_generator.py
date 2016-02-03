from itertools import izip

def generate(raw, tokenized, final_input):

    l=[]

    f=open(raw,'r')

    for i in f:

        i=i.strip().split('\t')
        l.append(i[0]+'\t')

    f.close()

    f=open(tokenized,'r')

    c=0
    for i in f:

        i=i.strip().split('\t')
        l[c]=l[c]+i[0]+'\t'+i[1]+'\n'
        c+=1

    f.close()

    f=open(final_input,'w')

    for i in l:

        f.write(i)

    f.close()

if __name__ == '__main__':
    
    generate('../../dataset/raw_training_data.txt','../../dataset/tweets_training_tokenized.txt', '../../dataset/final_training_input.txt')
    generate('../../dataset/raw_testing_data.txt','../../dataset/tweets_testing_tokenized.txt', '../../dataset/final_testing_input.txt')
