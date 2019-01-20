def merge(ls):
    if len(ls)>1:
        mid=len(ls)//2
        l=ls[:mid]
        r=ls[mid:]
        merge(l)
        merge(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                ls[k]=l[i]
                i+=1
            else:
                ls[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            ls[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            ls[k]=r[j]
            j+=1
            k+=1
ls=[12, 11, 13, 5, 6, 7]
(merge(ls))
print(ls)
