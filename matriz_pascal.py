def geraPascal(T,n):
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                T[i][j] = 1
            elif i != 0 and j !=0:
                T[i][j] = T[i-1][j] + T[i-1][j-1] 
            print(T[i][j], end=" ")
        print("")

def main():
    n = int(input())
    T = [[1]*n for i in range(n)]
    geraPascal(T,n)
main()