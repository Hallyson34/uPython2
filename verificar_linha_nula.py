def verificarColunas(A,n):
    c = 0
    for j in range(n):
        soma = 0
        for i in range(len(A)):
            soma += A[i][j]
        if soma == 0:
            c += 1
    return c

def verificarLinhas(A,m):
    l = 0
    for i in range(m):
        soma = 0
        for j in range(len(A[0])):
            soma += A[i][j]
        if soma == 0:
            l +=1
    return l

def main():
    m, n = map(int,input().split())
    A = []
    for i in range(m):
        A.append(list(map(int,input().split())))
    l = verificarLinhas(A,m)
    c = verificarColunas(A,n)
    print(f"Linhas nulas: {l}\nColunas nulas: {c}")
main()    