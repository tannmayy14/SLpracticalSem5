#playfair

def generateMatrix(key):
    alphabet='ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key=''.join(dict.fromkeys(key))
    key=key.upper()
    key=key.replace("J","I")
    matrix=[]
    used=set()

    for char in key:
        if char not in used:
            used.add(char)
            matrix.append(char)
    for char in alphabet:
        if char not in used:
            used.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0,25,5)]


def prepareText(text):
    text=text.replace("J","I").upper()
    text="".join(text.split())

    digraphs=[]
    i=0
    while i<len(text):
        a=text[i]
        b=text[i+1] if i+1<len(text) else 'X'
        if a==b:
            b="X"
        digraphs.append((a,b))
        i+=2
    return digraphs

def find_position(matrix,char):
    for r,row in enumerate(matrix):
        if char in row:
            return r,row.index(char)
    return None

def playfair(text,key,encrypt=True):
    matrix=generateMatrix(key)
    digraphs=prepareText(text)
    result=[]

    for a,b in digraphs:
        row1,col1=find_position(matrix,a)
        row2,col2=find_position(matrix,b)

        if row1==row2:
            if encrypt:
                result.append(matrix[row1][(col1+1)%5])
                result.append(matrix[row2][(col2+1)%5])
            else:
                result.append(matrix[row1][(col1-1)%5])
                result.append(matrix[row2][(col2-1)%5])
        elif col1==col2:
            if encrypt:
                result.append(matrix[(row1+1)%5][col1])
                result.append(matrix[(row2+1)%5][col2])
            else:
                result.append(matrix[(row1-1)%5][col1])
                result.append(matrix[(row2-1)%5][col2])
        else:
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])

    return "".join(result)

print(playfair("the key is hidden under the door pad","guidance",encrypt=True))
print(playfair("POCLBXDRLGIYBCGCIBSPLNAMLTTGIY","guidance",encrypt=False))
