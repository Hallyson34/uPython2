def fat(n):
    fatorial = 1
    for i in range(1, n+1):
	    fatorial = fatorial * i
    
    return fatorial

def imprimeTrianguloPascal(m):
    for n in range(0, m):
        for k in range(0, n+1):
            comb = fat(n) // (fat(k) * fat(n-k))
            print(comb, end=" ")
        
        print("")

def main():
    m = int(input())

    imprimeTrianguloPascal(m)

main()