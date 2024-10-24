"""def vignereEncrypt(p,k):
    p=p.replace(" ","").upper()
    k=k.replace(" ","").upper()
    k=(k*(len(p)//len(k) +1))[:len(p)].upper()

    encryptedText=''
    for kchar,pchar in zip(k,p):
        if pchar.isalpha():
            shift=ord(kchar)-ord('A')
            base=ord('A')
            encryptedText+=chr((ord(pchar)+shift-base)%26+base)
    return encryptedText
print(vignereEncrypt("She is listening","pascal"))

def vignereDecrypt(c,k):
    c=c.replace(" ","").upper()
    k=k.replace(" ","").upper()
    k=(k*(len(c)//len(k) +1))[:len(c)].upper()
    decryptedText=""
    for kchar,cchar in zip(k,c):
        if c.isalpha:
            shift=ord(kchar)-ord('A')
            base=ord('A')
            decryptedText+=chr((ord(cchar)-shift-base)%26 +base)
    print(decryptedText)

vignereDecrypt("HHWKSWXSLGNTCG","pascal")"""

def vignereE(ptext,key):
    ptext=ptext.replace(" ","").upper()
    key=key.replace(" ","").upper()
    key=(key*(len(ptext)//len(key) +1))[:len(ptext)].upper()

    encryptedText=""

    for pchar,kchar in zip(ptext,key):
        if pchar.isalpha():
            shift=ord(kchar)-ord('A')
            base=ord('A')
            encryptedText+=chr((ord(pchar)+shift-base)%26 +base)
    print(encryptedText)
def vignereD(ctext,key):
    ctext=ctext.replace(" ","").upper()
    key=key.replace(" ","").lower()
    key=(key*(len(ctext)//len(key) +1))[:len(ctext)].upper()

    decryptText=""

    for cchar,kchar in zip(ctext,key):
        if cchar.isalpha():
            shift=ord(kchar)-ord('A')
            base=ord('A')
            decryptText+=chr((ord(cchar)-shift-base)%26 +base)
    print(decryptText)
vignereE("Tanmay Bhatkar","pascal")

vignereD("IAFOAJQHSVKLG","pascal")
            
