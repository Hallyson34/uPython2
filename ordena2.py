def indiceMenor(v,i):
    menor = v[i]
    imenor = i
    for i in range(i+1,len(v)):
        if v[i]<menor:
            menor = v[i]
            imenor = i
    return menor,imenor

def indiceMaior(v,i):
    maior = v[i]
    imaior = i
    for i in range(i+1,len(v)):
        if v[i]>maior:
            maior = v[i]
            imaior = i
    return maior,imaior

def ordenaD(v):
    for i in range(len(v)-1):
        m,p = indiceMaior(v,i)
        aux = v[i]
        v[p] = aux
        v[i] = m

def ordena2(v):
    for i in range(len(v)):
        m,p = indiceMenor(v,i)
        aux = v[i]
        v[p] = aux
        v[i] = m


def main():
    v = list(map(int,input().split()))
    ordena2(v)
    print(v)
    ordenaD(v)
    print(v)

main()