#DH
def isPrime(n):
    flag=False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            flag=True
    if not flag:
        return True
    else:
        return False
    
def DH(alpha,q,XA,XB):
    if not(isPrime(q) and alpha<=q and XA<=q and XB<=q):
        raise ValueError("INVALID VALUES OF q,alpha,XA or XB")

    global YA,YB
    YA=pow(alpha,XA,q)
    YB=pow(alpha,XB,q)

    KA=pow(YB,XA,q)
    KB=pow(YA,XB,q)

    assert KA==KB,"ERROR///!: SHARED KEYS ARE NOT EQUAL!!!!!"
    print(f"""Public Key of A: {YA}
Public Key of B: {YB}
Shared Private Key: {KA}""")

def main():
    print("DiffieHellman Key Exchange")
    q=int(input("Enter your value of q: "))
    XA=int(input("Enter your value of XA: "))
    XB=int(input("Enter your value of XB: "))
    alpha=int(input("Enter your value of alpha: "))

    DH(alpha,q,XA,XB)
    
if __name__=="__main__":
    main()
    
