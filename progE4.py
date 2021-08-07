def trocaSecundaria(M,x):
	n = len(M)
	for i in range(0,n,4):
		for j in range(x,x-4,-1):
			M[i][j] = (n**2 + 1) - M[i][j]
			i+=1

def trocaPrincipal(M,x):
	n = len(M)
	for i in range(0,n,4):
			for j in range(x,x+4):
				M[i][j] = (n**2 + 1) - M[i][j]
				i+=1 
	
def Caso1(n, M):

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