def isPrime(num):
    flag=False
    if num==2:
        return False
    for i in range(2,num):
        if num%i==0:
            flag=True
    if not flag:
        return True
    else:
        return False
def dh(XA,XB,q,alpha):
    if XA>q or XB>q or alpha>q or not(isPrime(q)):
        print("XA or XB or q have invalid value")
        raise ValueError
    YA=pow(alpha,XA,q)
    YB=pow(alpha,XB,q)

    sharedKeyA=pow(YB,XA,q)
    sharedKeyB=pow(YA,XB,q)

    assert sharedKeyA==sharedKeyB,"NOT MATCHING KEYS!!"

    return(YA,YB,sharedKeyA)

print(dh(3,6,23,7))
