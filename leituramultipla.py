def calcCiclos(v,n):
    cont = 0
    ciclos = 0
    for i in range(len(v)):
        if v[i] == "R" and i<len(v)-1:
            if v[i+1] == "R" and cont<n:
                cont += 1
                if cont == n:
                    cont = 0
                    ciclos += 1    
            else:
                ciclos += 1
        elif v[i] != v[i-1] and i != 0:
            cont = 0
            ciclos += 1
        else:
            ciclos += 1
    return ciclos

def main():
    while True:
        try:
            text = list(input())
            n = int(input())
            print(calcCiclos(text,n))
        except EOFError:
            break
main()