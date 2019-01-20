def re(ls):
    xor=0
    for i in range(len(ls)):
        xor^=ls[i]
    for i in range(1,len(ls)):
        xor^=i
    return xor
print(re([1,2,3,1,4]))
