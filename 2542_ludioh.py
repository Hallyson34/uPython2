def main():
    while True:
        try:
            N = int(input())
            M, L = map(int,input().split())
            BM = []
            for i in range(M):
                BM.append(list(map(int,input().split())))
            BL = []
            for j in range(L):
                BL.append(list(map(int,input().split())))
            CM, CL = map(int,input().split())
            A = int(input())
            if BM[CM-1][A-1] > BL[CL-1][A-1]:
                print("Marcos")
            elif BL[CL-1][A-1] > BM[CM-1][A-1]:
                print("Leonardo")
            else:
                print("Empate")
        except EOFError:
            break
main()
