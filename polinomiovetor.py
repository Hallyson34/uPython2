def calcPoli(v, x):
    res = 0
    for i in range(0, len(v)):
        res += v[i] * x**i
    
    return res

#--------------------------------------------------

def main():
    vet = list(map(float, input().split()))
    n = int(input()) 
    for i in range(0, n):
        x = float(input())
        print(f"{calcPoli(vet, x):.4f}")

main()