def verificarCiclo(v,n):
    ciclos = 0
    i = 0
    while i < len(v): 
        if v[i] == "R":
            ciclos+=1
            j = i + 1
            cont = 1
            while j<len(v) and v[j] == "R" and cont < n:
                cont+=1
                j+=1 
            i = j
        else:
            ciclos+=1
            i += 1
    return ciclos    

#-------------------------------------

def main():
    while True:
        try:
            v = list(input())
            n = int(input())
            print(verificarCiclo(v,n))
        except EOFError:
            break
main()