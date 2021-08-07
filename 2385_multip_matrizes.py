#ERRO: Memory limit exceeded
def multiplicaAB(A,B,C):
    n = len(A)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                    C[i][j] += A[k][j] * B[i][k]

#-----------------------------------------------

def preencheAB(A, B, p, q, r, s, x, y):
    n = len(A)
    for i in range(n):
        for j in range(n):
            A[i][j] = (p * i + q * j)%x
            B[i][j] = (r * i + s * j)%y

#----------------------------------------------

def main():
    n = int(input())
    p,q,r,s,x,y = map(int, input().split())
    ic,jc = map(int, input().split())
    A=[[0] * n for i in range(n)]
    B=[[0] * n for i in range(n)]
    C=[[0] * n for i in range(n)]
    preencheAB(A, B, p, q, r, s, x, y)
    multiplicaAB(A,B,C)
    print(f"{C[ic-1][jc-1]}")
main()