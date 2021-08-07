def ordenando(vet):
    ordenado = [0] * len(vet)
    for valor in vet:
        cont = 0
        for i in range(len(vet)):
            if valor>vet[i]:
                cont += 1
        ordenado[cont] = valor 
    return ordenado
         
#-------------------------------------------

def main():
    v = list(map(int, input().split()))

    print(ordenando(v))
main()