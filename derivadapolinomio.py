def calcDeriv(v, d):
    for i in range(0, len(v)):
        d.append(i*v[i])

#---------------------------------------------------

def imprime(d):
    for i in range(1, len(d)):
        print(f"{d[i]:.4f}")

#---------------------------------------------------

def main():
    res = []
    vet = list(map(float, input().split()))
    calcDeriv(vet, res)
    imprime(res)

main()