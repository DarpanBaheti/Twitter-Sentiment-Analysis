f=open('raw_testing_data.txt')
for i in f:
    i=i.split('\t')
    print i[0]
    print i[1]
    break
f.close()
