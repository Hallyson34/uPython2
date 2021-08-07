def calcProd(u, v):
    produto = 0
    for i in range(0, len(u)):
        produto = produto + u[i]*v[i]
        
    return produto

#-------------------------------------------------

def main():
    u = list(map(float, input().split()))
    v = list(map(float, input().split()))
    print(f"{calcProd(u, v):.4f}")

main()
