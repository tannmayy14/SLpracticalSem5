#vignere
"""def vignereE(ptext,code):
    result=""
    ptext=ptext.replace(" ","").upper()
    code=code.replace(" ","").upper()
    code=(code*(len(ptext)//len(code)+1))[:len(ptext)].upper()

    for(pchar,cchar) in zip(ptext,code):
        if pchar.isalpha():
            result+=chr((ord(pchar)+ord(cchar)-ord('A')-ord('A'))%26 +ord('A'))
        else:
            result+=pchar

    return result

def vignereD(ctext,code):
    ctext=ctext.replace(" ","").upper()
    code=code.replace(" ","").upper()

    code=(code*(len(ctext)//len(code) +1))[:len(ctext)].upper()
    result=""

    for (ctchar,cchar) in zip(ctext,code):
        if ctchar.isalpha():
            result+=chr((ord(ctchar)-ord('A')-ord(cchar)+ord('A'))%26 +ord('A'))
        else:
            result+=ctchar

    return result
                                           
def main():
    code=input("Enter the code word: ").strip()
    ptext=input("Enter the plaintext: ").strip()
    print("Your encrypted word is ",vignereE(ptext,code))

    ctext=input("Enter the ciphertext: ").strip()
    print("Your decrypted word is ",vignereD(ctext,code))

if __name__=="__main__":
    main()"""
