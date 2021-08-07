def calcDireita(A,o,n):
    soma = 0
    cont = 0
    for j in range(n-1,(n//2),-1):
        for i in range(n-j,j):
            soma += A[i][j]
            cont += 1 
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
    print(f"{calcDireita(A,o,n):.1f}")
main()