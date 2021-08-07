#Lê frase e ordena de acordo com tabela ASCII(ordem aldabética)
def ordenar(v):
    for i in range(1, len(v)):
        mandante = v[i]
        j = i - 1
        while j >= 0 and v[j] > mandante:
            v[j+1] = v[j] 
            j -= 1
        v[j+1] = mandante
    return "".join(v)

#-----------------------------------------------

def main():
    frase = list(input())
    print(ordenar(frase))
main()