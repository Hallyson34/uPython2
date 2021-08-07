def calcSuperior(A,o):
    soma = 0
    cont = 0
    for i in range(len(A)//2):
        for j in range(i+1,(len(A)-1)-i):
            soma += A[i][j]
            cont += 1
            print(i)
    if o == "S":
        return soma
    else:
        return soma/cont

def main():
    o = input()
    n = 4
    A = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input())
    print(f"{calcSuperior(A,o):.1f}")
main()