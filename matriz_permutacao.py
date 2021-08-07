def verificaLinha(A,n,i):
    cont0 = 0
    cont1 = 0
    for j in range(n):
        if A[i][j] == 0:
            cont0+=1
        elif A[i][j] == 1:
            cont1+=1
        else:
            return False
    if cont0 == n-1 and cont1 == 1:
        return True
    else:
        return False

def verificaColuna(A,n,j):
    cont0 = 0
    cont1 = 0
    for i in range(n):
        if A[i][j] == 0:
            cont0+=1
        elif A[i][j] == 1:
            cont1+=1
        else:
            return False
    if cont0 == n-1 and cont1 == 1:
        return True
    else:
        return False

def main():
    n = int(input())
    A= []
    for i in range(n):
        A.append(list(map(int, input().split())))
    for k in range(n):    
        l = verificaLinha(A,n,k)
        c = verificaColuna(A,n,k)
        if l == False or c == False:
            print("Não é matriz permutação")
            break
    if l == True and c == True:
        print("é matriz permutação")
main()