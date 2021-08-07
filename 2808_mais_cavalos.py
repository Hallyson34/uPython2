def verificaTabuleiro(i,f):
    mi = int(i[1])-1 
    ni = ord(i[0])-97
    mf = int(f[1])-1
    nf = ord(f[0])-97
    for i in range(1,3):
        if mf == mi+1:
            if nf == ni+2 or nf == ni-2:
                return True
            else:
                return False
        elif mf == mi+2:
            if nf == ni+1 or nf == ni-1:
                return True
            else:
                return False
        elif mf == mi-1:
            if nf == ni+2 or nf == ni-2:
                return True
            else:
                return False
        elif mf == mi-2:
            if nf == ni+1 or nf == ni-1:
                return True
            else:
                return False
        else:
            return False
def main():
    i, f = map(str,input().split())
    
    if verificaTabuleiro(i,f):
        print("VALIDO")
    else:
        print("INVALIDO")
main()
