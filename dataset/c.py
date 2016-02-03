f=open('testingDatasetProcessed.txt','r')
f1=open('raw_testing_data.txt','w')
for i in f:
    i=i.split('\t')
    f1.write(i[2].strip()+'\t'+i[3].strip()+'\n')
f.close()
f1.close()
