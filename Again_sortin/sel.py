def sel(ls):
    for i in range(len(ls)):
        min_id=i
        for j in range(i+1,len(ls)):
            if ls[min_id]>ls[j]:
                min_id=j
        ls[i],ls[min_id]=ls[min_id],ls[i]
    return ls

print(sel([64,25,12,22,11]))



def ins(ls):
    for i in range(1,len(ls)):
        key=ls[i]
        j=i-1
        while j>=0 and key<ls[j]:
