def geraMatriz(M):
    n = len(M)
    #Preenche a diagonal principal com 2
    for x in range(n):
            M[x][x] = 2

    #Preenche a diagonal secundária com 3 
    j = n -1
    for i in range(n):
            M[i][j] = 3
            j-=1
    #Adicionando camadas de 1
    pos1 = n//3
    for i in range(pos1,n-pos1):
        for j in range(pos1,n-pos1):
            M[i][j] = 1

    #Adicionando 4 no centro
    half = (n //2)
    M[half][half] = 4

#-----------------------------------------------

def imprime(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            print(f"{M[i][j]}", end="")
        print("")
    
    print("")
        
#-----------------------------------------------        

def main():
    while True:
        try:
            n = int(input())
            M = [[0] * n for i in range(n)]
            geraMatriz(M)
            imprime(M)
        except EOFError:
            break
main()