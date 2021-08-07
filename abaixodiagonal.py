def somarTermos(A,t):
    soma = 0
    cont = 0
    for i in range(1,len(A)):
        for j in range(i):
            soma += A[i][j]
            cont+=1
    if t == "S":
        return soma
    else:
        return soma/cont
def main():
    t = input()
    n = 12
    A = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input())
    valor = somarTermos(A,t)
    print(f"{valor:.1f}")
main()