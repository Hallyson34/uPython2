def criptografar(v):
    for i in range(len(v)):
        if v[i] != " " and type(v[i]) != str:
            v[i] = chr(v[i]+97)
    return "".join(v)

#--------------------------------------------------------

def trocarValores(C,p,ch):
    n = len(p)
    vogal = True
    cripto = [0]*n
    vogais = ["a","e","i","o","u"]
    i = 0
    while i < len(p):
        if i == 0:
            k = 0
            while k < len(vogais):
                if p[i] == vogais[k]:
                    while i != n and p[i] != " ":
                        cripto[i] = p[i]
                        i += 1
                        k = 10
                k+=1
        if i<n and p[i] == " " and vogal:
            cripto[i] = p[i] 
            k = 0
            i+=1
            while k < len(vogais):
                if p[i] == vogais[k]:
                    while i != n and p[i] != " ":
                        cripto[i] = p[i]
                        i += 1
                        k = 10
                k+=1
        if k == 11:
            i-=1
        else:
            vogal = False
        if i < n and vogal == False:
            l = ord(ch[i]) - 97
            c = ord(p[i]) - 97
            if c != -65:
                cripto[i] = C[l][c]
            else:
                cripto[i] = " "
            vogal = True
        i+=1

    return cripto

#----------------------------------------------------------------

def geraCifra():
    Cifra = [[0]*26 for i in range(26)]
    for i in range(26):
        num = i
        for j in range(26):
            if num > 25:
                num -= 26 
            Cifra[i][j] = num
            num += 1
    return Cifra

#--------------------------------------------------------------

def organizaPalavra(p,c):
    n = len(p)
    vogal = True
    vogais = ["a","e","i","o","u"]
    repeticao = [0]*n
    for i in range(n):
        repeticao[i] = p[i]
    i = 0
    j = 0
    while i < n:
        if i == 0:
            k = 0
            while k < len(vogais):
                if repeticao[i] == vogais[k]:
                    while i != n and repeticao[i] != " ":
                        i += 1
                        k = 10
                k+=1
        while i<n and repeticao[i] == " " and vogal:
            k = 0
            i+=1
            while k < len(vogais):
                if repeticao[i] == vogais[k]:
                    while i != n and p[i] != " ":
                        i += 1
                        k = 10
                k+=1
        if k == 11:
            i-=1
        else:
            vogal = False
        while i < n and vogal == False:
            repeticao[i] = c[j]
            i+=1
            j+=1
            if j == len(c):
                j = 0
            if i<n and repeticao[i] == " ":
                i-=1
                break
        vogal = True
        i+=1

    return repeticao

#-----------------------------------------------------------------

def main():
    chave = list(input())
    n = int(input())
    for i in range(n):
        palavra = list(input())
        Cifra = geraCifra()
        pchave = organizaPalavra(palavra,chave)
        cripto = trocarValores(Cifra,palavra,pchave)
        print(criptografar(cripto))
main()