def geraMatriz(M):
    n = len(M)
    #Preenche a diagonal principal com 1
    for x in range(n):
            M[x][x] = 1

    #Preenche a diagonal secundária com 2 
    j = n -1
    for i in range(n):
            M[i][j] = 2
            j-=1

#-----------------------------------------------

def imprime(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            print(f"{M[i][j]}", end="")
        print("")
        
#-----------------------------------------------        

def main():
    while True:
        try:
            n = int(input())
            M = [[3] * n for i in range(n)]
            geraMatriz(M)
            imprime(M)
        except EOFError:
            break
main()