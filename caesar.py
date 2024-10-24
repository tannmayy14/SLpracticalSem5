def encrypt(text,s):
    result=""
    for i in range(len(text)):
        c=text[i]

        if c.isupper():
            result+=chr((ord(c)+s-65)%26+65)
        elif c.islower():
            result+=chr((ord(c)+s-97)%26+97)
        else:
            result+=c
    return result

def decrypt(text,s):
    result=""
    for i in range(len(text)):
        c=text[i]
        if c.isupper():
            result+=chr((ord(c)-s-65)%26+65)
        elif c.islower():
            result+=chr((ord(c)-s-97)%26+97)
        else:
            result+=c
    return result

print(encrypt('tanmay',3))
print(decrypt(encrypt('tanmay',3),3))

    
