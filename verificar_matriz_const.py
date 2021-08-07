def verificarConstante(r):
    n = len(r)
    for i in range(n-1):
        if r[i] != r[i+1]:
            return False
    return True
        

def somaColunas(M,r):
    n = len(M)
    for j in range(n):
        soma = 0
        for i in range(n):
            soma += M[i][j]
        print(f"{soma} colunas")
        r.append(soma)
    return soma


def somaLinhas(M,r):
    n = len(M)
    for i in range(n):
        soma = 0
        for j in range(n):
            soma += M[i][j]
        print(f"{soma} linhas")
        r.append(soma)
    return soma

def somaDiagonalS(M,r):
    soma = 0
    n = len(M)
    j = n-1
    for i in range(n):
        soma += M[i][j]
        j-=1
    r.append(soma)
    return soma

def somaDiagonalP(M,r):
    soma = 0
    n = len(M)
    for i in range(n):
        soma += M[i][i]
    r.append(soma)
    return soma
        
def main():
    M = []
    resultados = []
    while True:
        try:
            linha = list(map(int,input().split()))
            M.append(linha)
        except EOFError:
            break
    print(somaDiagonalP(M,resultados))
    print(somaDiagonalS(M,resultados))
    print(somaLinhas(M,resultados))
    print(somaColunas(M,resultados))
    if verificarConstante(resultados):
        print("É constante")
    else:
        print("Não é constante")
main()