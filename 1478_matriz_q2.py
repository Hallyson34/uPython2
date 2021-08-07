def geramatriz(M):
    n = len(M)
    #Constrói linhas de 1 até n
    for i in range(n):
        val = 1
        for j in range(i, n):
            M[i][j] = val
            val += 1
    
    #Constrói colunas de 1 até n
    for j in range(n):
        val = 1
        for i in range(j,n):
            M[i][j] = val
            val += 1

#----------------------------------------------

def imprime(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            fim = " " if j != n - 1 else ""
            print(f"{M[i][j]:>3}", end=fim)
        print("")

    print("")

#---------------------------------------------

def main():
    n = int(input())
    while n != 0:
        M = [[0] * n for i in range(n)]
        geramatriz(M)
        imprime(M)

        n = int(input())
main()