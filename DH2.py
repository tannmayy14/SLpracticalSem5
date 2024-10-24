def isPrime(num):
    flag=False
    if num==2:
        return True
    for i in range(2,num):
        if num%i==0:
            flag=True
    if not flag:
        return True
    else:
        return False

def DH(q,alpha,XA,XB):
    if not(isPrime(q)) or alpha>q or XA>q or XB>q:
        print("INVALID VALUE OF q,alpha or XA,XB")
        raise ValueError
    YA=pow(alpha,XA,q)
    YB=pow(alpha,XB,q)
    SharedKeyA=pow(YB,XA,q)
    SharedKeyB=pow(YA,XB,q)

    assert SharedKeyA==SharedKeyB,"Shared Keys do not match"

    print(f"""YA(public Key of A): {YA}
YB(public Key of B): {YB}
Shared Key: {SharedKeyA} """)

DH(7,3,2,5)
