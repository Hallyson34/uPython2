#Usado em Caso 3
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

#--------------------------------------------------------

#Usado em Caso 2
def trocaSecundaria(M,x):
	n = len(M)
	for i in range(0,n,4):
		for j in range(x,x-4,-1):
			M[i][j] = (n**2 + 1) - M[i][j]
			i+=1

#--------------------------------------------------------

#Usado em Caso 2
def trocaPrincipal(M,x):
	n = len(M)
	for i in range(0,n,4):
			for j in range(x,x+4):
				M[i][j] = (n**2 + 1) - M[i][j]
				i+=1 
	
#--------------------------------------------------------

def Caso1(n, M):
	print("Caso 1:")

	# <CODIGO>
	i = 0
	j = n // 2
	M[i][j] = 1
	for x in range(2, n*n + 1):
		anti = i
		antj = j
		i = i - 1
		j = j + 1
		if i == -1 or j == n:
			if i == -1:
				i = n - 1
				if j == n:
					j = 0
			else:
				j = 0
		if M[i][j] == 0: 
			M[i][j] = x
		else:
			j = antj
			i = anti + 1
			if i == n:
				i = 0
			M[i][j] = x

	# </CODIGO>


# =========================================


def Caso2(n, M):
	print("Caso 2:")

	# <CODIGO>
	#Construindo matriz
	num = 0
	for i in range(n):
		for j in range(n):
			num+=1
			M[i][j] = num
			
	#Substituindo Diagonais
	j = 0
	k = 3
	for c in range(n//4):
		trocaPrincipal(M,j)
		j+=4
		trocaSecundaria(M,k)
		k+=4

	# </CODIGO>


# =========================================


def Caso3(n, M):
	print("Caso 3:")

	# <CODIGO>
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


	# </CODIGO>
	
			
# =========================================


# == NÃO ALTERE ESTA FUNÇÃO ===============
def imprimeM(n, M):
	for i in range(n):
		for j in range(n):
			print(M[i][j], end="\t")
		print("")

		
# =========================================


# == NÃO ALTERE ESTA FUNÇÃO ===============
def main():
	# Leitura da entrada
	n = int(input())

	# Cria uma matriz quadrade de ordem n preenchida com 0's
	M = [[0] * n for i in range(n)]

	if n % 2 == 1:
		Caso1(n, M)
	elif n % 4 == 0:
		Caso2(n, M)
	else:
		Caso3(n, M)

	# Esta função não deve ser alterada.
	imprimeM(n, M)

main()
# =========================================