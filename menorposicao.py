def calcMenor(v):
    menor = v[0]
    pos = 0
    for i in range(1,len(v)):
        if v[i] < menor:
            menor = v[i]
            pos = i
    return menor,pos
        

def main():
    n = int(input())
    vet = list(map(int,input().split()))
    m,p = calcMenor(vet)
    print(f"Menor valor: {m}\nPosicao: {p}")
main()