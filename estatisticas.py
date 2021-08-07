
#---------------------------------------------------

def calcMedia(vet):
    media = 0
    soma = 0
    for i in range(len(vet)):
        soma += vet[i]
    media = soma/len(vet)

    return media

#---------------------------------------------------

def calcVariancia(vet,m):
    soma = 0
    for valor in vet:
        soma += (valor-m) ** 2

    return soma / len(vet)
#-------------------------------------------------  

def calcDesvio(var):
    return var ** (1/2)

#-------------------------------------------------

def calcMaior(vet):
    maior = vet[0]
    for i in range(1,len(vet)):
        if vet[i]>maior:
            maior = vet[i]

    return maior

#-------------------------------------------------

def calcMenor(vet):
    menor = vet[0]
    for i in range(1,len(vet)):
        if vet[i]<menor:
            menor = vet[i]
    
    return menor

#----------------------------------------------

def main():
    v = list(map(float, input().split()))

    maiorv = calcMaior(v)
    menorv = calcMenor(v)
    mediav = calcMedia(v)
    varv = calcVariancia(v,mediav)
    desviov = calcDesvio(varv)
    print(f"O maior número é: {maiorv}, o menor é: {menorv}, a média é: {mediav:.2f}, a variancia é: {varv:.2f}, e o desvio padrão é: {desviov:.2f}")
main()