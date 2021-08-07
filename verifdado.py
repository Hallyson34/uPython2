def contaFace(exp, face):
    for f in exp:
        face[f] +=1
#----------------------------------
def imprime(face):
    for i in range (1, len(face)):
        print(f"{i}: {face[i]} vezes.")
#---------------------------------
def main():
    exp = list(map(int, input().split()))
    face = [0] * 7
    contaFace(exp, face)
    imprime(face)
main()
