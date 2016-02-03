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
            tweet[i]=''.join(l).strip()

    return tweet, cnt

print replace_repetition(["I","looool","coooooool"])
