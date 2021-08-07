def transposta(A,m,n):
    T = [[0]*m for i in range(n)]

    for i in range(m):
        for j in range(n):
            T[j][i] = A[i][j]
            
    return T

def imprime(T,n,m):
    for i in range(n):
        for j in range(m):
            print(T[i][j], end=" ")
        print("")

def main():
    m ,n = map(int, input().split())
    A = []
    for i in range(m):
        A.append(list(map(int, input().split())))
    T = transposta(A, m, n)
    imprime(T, n, m)
main()