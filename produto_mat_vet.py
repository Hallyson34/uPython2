def calcProduto(A, v, m, n):
    u = [0]*m
    for i in range(m):
        soma = 0
        for j in range(n):
           soma += A[i][j] * v[j]
        u[i] = soma    
    return u

def main():
    m, n = map(int, input().split())
    A = []
    for i in range(m):
        A.append(list(map(int, input().split())))

    v = list(map(int, input().split()))
    print(calcProduto(A, v, m, n))
main()