#Produto entre Matrizes
#A[m][n] X B[n][p] = C[m][p]
def calculaProduto(A,B,C):
    print("Resultado: ")
    for i in range(len(C)):
        for j in range(len(C[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]
            print(C[i][j], end=" ")
        print("")

def main():
    m, n, p = map(int, input().split())
    A = []
    for i in range(m):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(n):
        B.append(list(map(int, input().split())))
    C = [[0] * p for i in range(m)]
    calculaProduto(A,B,C)
    
main() 