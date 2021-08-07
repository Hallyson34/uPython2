def criarVetor(vetor1):
    for i in range(0, 20):
        n = int(input())
        vetor1[i] = n
#-----------------------------------------
def trocarTermos(vetor1, vetor2):
    inv = len(vetor1)-1
    for j in range(0, 20):
        vetor2[j] = vetor1[inv]
        print(f"N[{j}] = {vetor2[j]}")
        inv -= 1
#-----------------------------------------
def main():
    vet1 = [0] * 20
    vet2 = [0] * 20
    criarVetor(vet1)
    trocarTermos(vet1, vet2)
#-----------------------------------------
main()