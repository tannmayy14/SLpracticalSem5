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
    while(b!=0):
        a,b=b,a%b
    return a

def GenerateKeys():
    p=int(input("Enter p: "))
    if not (isPrime(p)):
        print("p is not a prime number")
        raise ValueError
    q=int(input("Enter q: "))
    if not (isPrime(q)):
        print("q is not a prime number")
        raise ValueError
    global n
    n=p*q
    phi=(p-1)*(q-1)

    global e
    e=int(input("Enter e: "))
    if (e>phi or e<1) or (gcd(e,phi)!=1):
          print("Invalid value of e")
          raise ValueError

    global d
    d=pow(e,-1,phi)
    publicKey=(e,n)
    privateKey=(d,n)

    print(f"""Your Public key is: {publicKey}
And your Private Key is: {privateKey} """)

GenerateKeys()

def encryption():
    plaintext=int(input("plaintext: "))
    global e,n
    enc=pow(plaintext,e,n)
    print(enc)

def decryption():
    ciphertext=int(input("ciphertext"))
    global d,n
    dec=pow(ciphertext,d,n)
    print(dec)
decryption()
