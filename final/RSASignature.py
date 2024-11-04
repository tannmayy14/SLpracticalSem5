#RSA DIGITAL SIGNATURE
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
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def generateKeys():
    p=int(input("Enter prime number p:"))
    q=int(input("Enter prime number q:"))

    if not(isPrime(p) and isPrime(q)):
        raise ValueError("p&q should be prime number!!!!")
    
    global e,n,d,phi
    n=p*q
    phi=(p-1)*(q-1)

    e=int(input(f"Enter value for e such that 1<e<{phi} and gcd(e,{phi})=1: "))
    if not(1<e<phi and gcd(e,phi)==1):
        raise ValueError("Invalid value of e")

    d=pow(e,-1,phi)
    publicKey=(e,n)
    privateKey=(d,n)

    print(f"""Public Key: {publicKey}
Private Key: {privateKey}""")

def signMessage():
    M=int(input("Enter message to be signed: "))
    global d,n
    S=pow(M,d,n)
    print(f"Digital Signature of your message is: {S}")
def verifyMessage():
    S=int(input("Enter the signed message received: "))
    M=int(input("Enter the original message: "))
    global e,n
    Md=pow(S,e,n)
    print(f"Verified Message: {Md}")
    if M==Md:
        print("Message verified correctly")
        print("Signature Valid")
    else:
        print("Message not verified")
        print("Signature Invalid")

ch=0
while ch!=4:
    print("1)GENERATE KEYS\n2)signMessage\n3)verifyMessage\n4)EXIT")
    ch=int(input("Enter your choice: "))
    if ch==1:
        generateKeys()
    if ch==2:
        try:
            signMessage()
        except:
            print("GENERATE KEYS FIRST!!!!!!!!!!!!!!!")
    if ch==3:
        try:
            verifyMessage()
        except:
            print("GENERATE KEYS FIRST!!!!!!!!!!!!!!!")
    if ch==4:
        exit()
