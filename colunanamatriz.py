def somarColuna(A,c,t):
    soma = 0
    for i in range(len(A)):
        soma+=A[i][c]
    if t == "S":
        print(soma)
    else:
        print(soma/len(A))

def main():
    c = int(input())
    t = input()
    n = 3
    A = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = float(input())
    print(A)
    somarColuna(A,c,t)
main()
        