def calcDiagonal(A,o,n):
    soma = 0
    cont = 0
    for i in range(n-1):
        for j in range(n-1-i):
            soma += A[i][j]
            cont += 1
    if o == "S":
        return soma
    else:
        return soma/cont
def main():
    o = input()
    n = 12
    A = [[0]*n for i in range(n)]
    for  i in range(n):
        for j in range(n):
            A[i][j] = float(input())
    print(f"{calcDiagonal(A,o,n):.1f}")
main()