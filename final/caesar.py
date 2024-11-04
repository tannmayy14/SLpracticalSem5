#caesar

def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]

        if char.isupper():
            result+=chr((ord(char)-65+s)%26 +65)
        elif char.islower():
            result+=chr((ord(char)-97+s)%26 +97)
        else:
            result+=char
    result=result.upper()
    return result

def decrypt(text,s):
    result=""

    for i in range(len(text)):
        char=text[i]

        if char.isupper():
            result+=chr((ord(char)-s-65)%26 +65)
        elif char.islower():
            result+=chr((ord(char)-s-97)%26+ 97)
        else:
            result+=char

    result=result.lower()
    return result

def main():
    ch=0
    while ch!=3:
        ch=int(input("Enter your choice\n1)Encrypt\n2)Decrypt\n3)Exit\nCHOICE: "))
        if ch==1:
            word=input("Enter your word to be encrypted: ").strip()
            key=int(input("Enter your key: "))
            print("Encrypted word is=> ")
            print(encrypt(word,key))
        elif ch==2:
            word=input("Enter your word to be decrypted: ").strip()
            key=int(input("Enter your key: "))
            print("Decrypted word is=> ")
            print(decrypt(word,key))
        elif ch==3:
            exit()
        else:
            print("Enter correct choice!!!!!!!")

if __name__=="__main__":
    main()
