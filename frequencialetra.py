def organiza(v):
    for i in range(len(v)):
        num = ord(v[i])
        if 64<num<91 or 96<num<123:
            if 64<num<91:
                num += 32
                v[i] = chr(num)
        else:
            v[i] = 0

#------------------------------------

def verRepetidos(v):
    cont = [0]*26
    for i in range(len(v)):
        if v[i] != 0:
            cont[ord(v[i])-97] += 1
    return cont

#------------------------------------

def contador(v):
    maior = v[0]
    pos = []
    for i in range(1,26):
        if v[i] > maior:
            maior = v[i]
    for j in range(26):
        if v[j] == maior:
            pos.append(j)
    return pos    
        
#-------------------------------------

def ordemABC(v):
    if len(v)>1:
        for i in range(len(v)):
            if i<len(v)-1:
                print(chr(v[i]+97), end="")
            else:
                print(chr(v[i]+97))        
    else:
        print(chr(v[0]+97))

#-------------------------------------

def main():
    t = int(input())
    for i in range(t):
        text = list(input())
        organiza(text)
        ordemABC(contador(verRepetidos(text)))
main()