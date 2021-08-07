def decifrarE(v):
    meio = len(v) // 2 
    j = meio - 1
    for i in range(meio // 2):
        aux = v[j]
        v[j] = v[i]
        v[i] = aux 
        j -= 1

def decifrarD(v):
    meio = len(v) // 2 
    j = len(v) - 1
    for i in range(meio, meio + meio // 2):
        aux = v[j]
        v[j] = v[i]
        v[i] = aux 
        j -= 1
    return "".join(v)
#-------------------------------

def main():
    n = int(input())
    for i in range(n):
        text = list(input())
        decifrarE(text)
        print(decifrarD(text))
main()