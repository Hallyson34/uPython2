def verificarNulo(A,m,n):
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                return print("Sim")
    return print("Não")
def main():
    m,n = map(int,input().split())
    A = []
    for i in range(m):
        linha = list(map(int,input().split()))
        A.append(linha)
    verificarNulo(A,m,n)
main()