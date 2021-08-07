def maiorColuna(A,m,maiorcol):
    for k in range(m):
        maior = -1
        for i in range(m):
            col = A[i][k]
            if col > maior:
                maior = col
        maiorcol.append(maior)

#-------------------------------------------------

def imprimeA(A,m,maior):
    for i in range(m):
        for j in range(m):
            t = len(str(maior[j]))
            fim = " " if j != m-1 else "" 
            print(f"{A[i][j]:>{t}}", end=fim)
        print("")
#-------------------------------------------------

def main():
    n = int(input())
    x = 4
    for i in range(n):
        m = int(input())
        A =[]
        maiorcol = []
        for j in range(m):
            A.append(list(map(int, input().split())))
            for k in range(len(A[j])):
                A[j][k] = A[j][k] ** 2
        maiorColuna(A,m,maiorcol)
        print(f"Quadrado da matriz #{x}:")
        imprimeA(A,m,maiorcol)
        if i != n-1:
            print("")
        x+=1
main()