def verificarParimp(A,m,n):
    par =0
    impar = 0
    for i in range(m):
        for j in range(n):
            if A[i][j] %2 == 0:
                par+=1
            else:
                impar +=1
    return par,impar
def main():
    m,n = map(int,input().split())
    A = []
    for i in range(m):
        linha = list(map(int,input().split()))
        A.append(linha)
    par,impar =verificarParimp(A,m,n)
    print(f"{par}Pares e {impar}Impares")
main()