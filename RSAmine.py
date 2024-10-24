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

def generateKeys():
    p=int(input("Enter prime number p: "))
    if (isPrime(p)==False):
          print("p is not a Prime Number")
          raise ValueError
        
    q=int(input("Enter prime number q: "))
    if (isPrime(q)==False):
          print("q is not a Prime Number")
          raise ValueError
    phi=(p-1)*(q-1)

    global n
    n=p*q

    global e
    e=int(input("Enter a value for e: "))
    if ((gcd(e,phi)!=1) and (e<1 or e>phi)):
        print("Invalid value of e!!!")
        raise ValueError

    global d
    d= pow(e,-1,phi)
    publicKey=(e,n)
    privateKey=(d,n)

    print(f"""Your Public key is: {publicKey}
And your Private Key is: {privateKey} """)

def encryption():
    plaintext=int(input("Enter plain text: "))
    global e,n
    encryptedtext=pow(plaintext,e,n)
    print(f"Your encrypted text is: {encryptedtext}")

def decryption():
    ciphertext=int(input("Enter plain text: "))
    if NameError:
        print()
    global d,n
    decryptedtext=pow(ciphertext,d,n)
    print(decryptedtext)

ch=0
while ch!=4:
    ch=int(input("1)KEY GENERATION,2)ENCRYPT 3)DECRYPTED"))
    if ch==1:
        generateKeys()
    elif ch==2:
        try:
            encryption()
        except:
            print("************GENERATE KEYS FIRST*****************")
            continue
    elif ch==3:
        try:
            decryption()
        except:
            print("************GENERATE KEYS FIRST*****************")
            continue
    if ch==4:
        print("CLOSING")
    
