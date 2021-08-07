def calcEsquerda(A,o,n):
    soma = 0
    cont = 0
    for j in range(n//2):
        for i in range(j+1,(n-1)-j):
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
    print(f"{calcEsquerda(A,o,n):.1f}")
main()