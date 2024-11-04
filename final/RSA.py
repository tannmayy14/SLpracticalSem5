#RSA
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

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def generateKeys():
    p=int(input("Enter prime number p: "))
    if not isPrime(p):
        raise ValueError("INCORRECT VALUE OF p,not a prime number")
    q=int(input("Enter prime number q: "))
    if not isPrime(q):
        raise ValueError("INCORRECT VALUE OF q,not a prime number")

    global n
    n=p*q

    global phi
    phi=(p-1)*(q-1)
    
    global e
    e=int(input("Enter appropriate value of e:"))
    if e>=phi or e<=1 or gcd(e,phi)!=1:
        raise ValueError("Incorrect value of e, 1<e<phi and gcd(e,phi)=1")

    publicKey=(e,n)

    global d
    d=pow(e,-1,phi)

    privateKey=(d,n)

    print(f"""Your public Key is {publicKey}
Your private key is {privateKey}""")


def encrypt():
    pt=int(input("Enter your plaintext: "))
    global e,n

    et=pow(pt,e,n)
    print(f"Encrypted text is: {et}")

def decrypt():
    ct=int(input("Enter your ciphertext: "))
    global d,n
    dt=pow(ct,d,n)
    print(f"Decrypted Text is: {dt}")
    
ch=0
while ch!=4:
    print("1)GENERATE KEYS\n2)ENCRYPT\n3)DECRYPT\n4)EXIT")
    ch=int(input("Enter your choice: "))
    if ch==1:
        generateKeys()
    if ch==2:
        try:
            encrypt()
        except:
            print("GENERATE KEYS FIRST!!!!!!!!!!!!!!!")
    if ch==3:
        try:
            decrypt()
        except:
            print("GENERATE KEYS FIRST!!!!!!!!!!!!!!!")
    if ch==4:
        exit()
        
    
