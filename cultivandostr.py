def tamStr(v):
    maior = 0
    for i in range(len(v)):
        j = 0
        cont = 0
        while j<len(v):
            if (v[i] in v[j]) == True:
                cont +=1
                if cont > maior:
                    maior = cont
            else:
                cont = 0
            j+=1
    return maior

#------------------------------------------

def main():
    verif = True
    while verif: 
        n = int(input())
        string = [1] * n
        for i in range(n):
            string[i] = input()
        if n == 0:
            verif = False 
            break      
        print(tamStr(string))
main()