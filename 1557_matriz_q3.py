def geraMatriz(M):
    n = len(M)
    #Constrói linhas de 1 até n
    for i in range(n):
        for j in range(i, n):
            val = 2 ** (j+i)
            M[i][j] = val
    
    #Constrói colunas de 1 até n
    for j in range(n):
        for i in range(j,n):
            val = 2 ** (i + j)
            M[i][j] = val

def imprime(M):
    n = len(M)
    ultimo = str(M[-1][-1])
    t = len(ultimo)
    for i in range(n):
	    for j in range(n):
		    fim = " " if j != n - 1 else ""
		    print(f"{M[i][j]:>{t}}", end=fim)
	    print("")

    print("")
def main():
    n = int(input())
    while n != 0:
        M = [[0] * n for i in range(n)]
        geraMatriz(M)
        imprime(M)


        n = int(input())
main()