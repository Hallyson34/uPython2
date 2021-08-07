def geraMatriz(M):
	n = len(M)

	half = (n + 1) // 2
	inicio = 0
	final = n-1
	for val in range(1, half + 1):
		for j in range(inicio,final+1):
			M[inicio][j] = val
			M[final][j] = val
		for i in range(inicio,final+1):
			M[i][inicio] = val
			M[i][final] = val
		inicio+=1
		final-=1
				 



#=====================================

def imprimeMatriz(M):
	n = len(M)
	for i in range(n):
		for j in range(n):
			fim = " " if j != n - 1 else ""
			print(f"{M[i][j]:>3}", end=fim)
		print("") # pula uma linha após imprimir uma linha inteira da matriz

	print("")

#=====================================

def main():
	n = int(input())

	while n != 0:
		M = [[-1] * n for i in range(n)]
		geraMatriz(M)
		imprimeMatriz(M)
		n = int(input())

main()