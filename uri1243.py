#O quão fácil é:
def mediaTamanhos(t):
    if len(t) == 0:
        return 0
    soma = 0
    for i in t:
        soma += i
    media = soma//len(t)
    if media <= 3:
        return 250
    elif media >= 6:
        return 1000
    else:
        return 500

#--------------------------------------------------

def medirPalavras(f):
    tamanhos = []
    i = 0
    verificador = False
    while i < len(f):
        tamp = 0
        while i<len(f) and ord(f[i]) > 64:
            tamp += 1
            verificador = True
            i += 1
        if verificador:
            tamanhos.append(tamp)
            verificador = False
            i-=1 
        i += 1
    return tamanhos

#-------------------------------------------------

def main():
    while True:
        try:
            frase = list(input())
            print(mediaTamanhos(medirPalavras(frase)))
        except EOFError:
            break
main()