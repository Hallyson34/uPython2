def verificarLetra(A,i,j,M,val):
    dbi = i + i
    dbj = j + j
    if A[i][j] == "L":
        M[dbi][dbj+1] = val
        M[dbi+1][dbj] = val + 1
        M[dbi+1][dbj+1] = val + 2
        M[dbi][dbj] = val + 3
        A[i][j] = 1
                
    elif A[i][j] == "X":
        M[dbi][dbj] = val
        M[dbi+1][dbj+1] = val + 1
        M[dbi+1][dbj] = val + 2
        M[dbi][dbj+1] = val + 3
        A[i][j] = 1
                      
    elif A[i][j] == "U":
        M[dbi][dbj] = val
        M[dbi+1][dbj] = val + 1
        M[dbi+1][dbj+1] = val + 2
        M[dbi][dbj+1] = val + 3
        A[i][j] = 1

#----------------------------------------------------

def preencheM(n, M):
    m = (n - 1) // 4
    half = n // 2
    #Criando Matriz Auxiliar == A
    A = [["L"] * half for i in range(half)]
    for i in range(m + 1,half):
        for j in range(half):
            if i == (m + 1):
                A[i][j] = "U"
            else:
                A[i][j] = "X"
    A[m][half // 2] = "U"
    A[m+1][half // 2] = "L"
    
    #Percorre Matriz Auxiliar
    i = 0
    j = half//2
    val = 1
    verificarLetra(A,i,j,M,val)
    val+=4
    while val <= (n*n):
        anti = i
        antj = j
        i = i - 1
        j = j + 1
        if i == -1 or j == half:
            if i == -1:
            	i = half - 1
            	if j == half:
            		j = 0
            else:
            	j = 0
        if A[i][j] != 1: 
            verificarLetra(A,i,j,M,val)
        else:
            j = antj
            i = anti + 1
            if i == half:
            	i = 0
            verificarLetra(A,i,j,M,val)
        val+=4

#-----------------------------------------------------

def imprimeM(n, M):
	for i in range(n):
		for j in range(n):
			print(M[i][j], end="\t")
		print("")

def main():
	n = int(input())
	M = [[0] * n for i in range(n)]
	preencheM(n, M)
	imprimeM(n, M)
main()
