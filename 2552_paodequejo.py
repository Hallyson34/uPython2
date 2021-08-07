def verificarPaes(P,n,m):
    for i in range(n):
        for j in range(m):
            if P[i][j] == 1:
                P[i][j] = 9
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if i != n-1 and k == 0 and P[i][j] !=9 and P[i+1][j] == 9:
                    P[i][j]+=1
                elif j != m-1 and k == 1 and P[i][j] !=9 and P[i][j+1] == 9:
                    P[i][j]+=1
                elif i != 0 and k == 2 and P[i][j] !=9 and P[i-1][j] == 9:
                    P[i][j]+=1
                elif j != 0 and k == 3 and P[i][j] !=9 and P[i][j-1] == 9:
                    P[i][j]+=1

def imprime(P, n, m):
    for i in range(n):
        for j in range(m):
            print(P[i][j], end="")
        print("")

def main():
    while True:
        try:
            n, m = map(int, input().split())
            P = []
            for i in range(n):
                P.append(list(map(int, input().split())))
            verificarPaes(P,n,m)
            imprime(P, n, m)
        except EOFError:
            break
main()