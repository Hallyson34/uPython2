def verificaMiniS(S,i):
    n = 0
    while n<9:
        num = [1,2,3,4,5,6,7,8,9]
        for m in range(i,i+3):
            for j in range(n,n+3):
                for l in range(len(num)):
                    if S[m][j] == num[l]:
                        num[l] = 0
        for k in num:
            if k != 0:
                return False
        n+=3
    return True

#-----------------------------------------------------------

def verificaLinha(S,i):
    num = [1,2,3,4,5,6,7,8,9]
    for j in range(9):
        for k in range(len(num)):
            if S[i][j] == num[k]:
                num[k] = 0
    for n in num:
        if n != 0:
            return False
    return True

#-----------------------------------------------------------

def verificaColuna(S,j):
    num = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        for k in range(len(num)):
            if S[i][j] == num[k]:
                num[k] = 0
    for n in num:
        if n != 0:
            return False
    return True

#-----------------------------------------------------------

def verificarSolucao(S):
    for i in range(9):
        if verificaLinha(S,i) == False:
            return False
        if verificaColuna(S,i) == False:
            return False
    for i in range(0,9,3):
        if verificaMiniS(S,i) == False:
            return False
    return True

#-----------------------------------------------------------

def main():
    n = int(input())
    S = [0]*9
    for i in range(1,n+1):
        for j in range(9):
            S[j] = list(map(int, input().split()))
        print(f"Instancia {i}")
        print("SIM") if verificarSolucao(S) == True else print("NAO")
        print("")
main()