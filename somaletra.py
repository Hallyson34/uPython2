def somarL(vet):
    soma = 0
    for i in range(0, len(vet)):
        soma += ord(vet[i])
    return soma    

#----------------------------------------------

def main():
    n = int(input("Quantos nomes quer digitar? "))
    for i in range(0,n):
        nome = input("Digite seu nome: ")
        nome_l = list(nome)
        print(somarL(nome_l))

main()

