def somarLinha(A,l):
    soma = 0
    for j in range(12):
        soma +=A[l][j]
    return soma

def main():
    l = int(input())
    t = input()
    A= [[0]*3 for k in range(12)]
    for i in range(3):
        for j in range(3):
            num = float(input())
            A[i][j] = num
    if t == "S":
        soma = somarLinha(A,l)
        print(soma)
    else:
        print(somarLinha(A,l)/3)
main()