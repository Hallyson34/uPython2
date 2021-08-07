def calcProduto(A,B,m,n,p):
    C = [[0]*p for i in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def main():
    m, n, p = map(int,input().split())
    A = []
    B = []    
    for i in range(m):
        A.append(list(map(int, input().split())))
    for i in range(n):
        B.append(list(map(int, input().split())))
    print(calcProduto(A,B,m,n,p))
main()