def somarMatrizes(A,B,C,m,n):
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    
def imprime(M,m,n):
	for i in range(m):
		for j in range(n):
			print(M[i][j], end="\t")
		print("")


def main():
    m ,n = map(int,input().split())
    A = []
    B = []
    C = [[0]*n for i in range(m)]
    for i in range(m):
            A.append(list(map(int,input().split())))
    for i in range(m):
            B.append(list(map(int,input().split())))
    somarMatrizes(A,B,C,m,n)
    imprime(C,m,n)
main()
     
