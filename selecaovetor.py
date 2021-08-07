def armazenar(vet):
    for i in range(0,100):
        n = float(input())
        vet[i] = n
        verificar(vet, i)

#--------------------------------------------------
def verificar(vetor,contador):
        if vetor[contador] <= 10:
           return print(f"A[{contador}] = {vetor[contador]:.1f}")
#--------------------------------------------------
def main():
    vet = []
    vet = [0] * 100
    armazenar(vet)
#--------------------------------------------------
main()