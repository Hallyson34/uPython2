def isPar(v,n):
        v.append(n)
        if len(v) == 5:
            for i in range(5):
                print(f"par[{i}] = {v[i]}")

#---------------------------------------------

def isImpar(v,n):
    v.append(n)
    if len(v) == 5:
        for i in range(5):
            print(f"impar[{i}] = {v[i]}")

#----------------------------------------------

def verificaSobras(impar,par):
    if len(par) != 0 or len(impar) !=0:
        if len(impar) != 0:
            for i in range(len(impar)):
                print(f"impar[{i}] = {impar[i]}")
            if len(par) !=0:
                for i in range(len(par)):
                    print(f"par[{i}] = {par[i]}") 
        elif len(par) !=0:
            for i in range(len(par)):
                print(f"par[{i}] = {par[i]}")

#----------------------------------------------

def main():
    par = []
    impar = []
    for i in range(15):
        num = int(input())
        if num % 2 == 0:
            isPar(par,num)
            if len(par) == 5:
                par = []
        else:
            isImpar(impar,num)
            if len(impar) == 5:
                impar = []
    verificaSobras(impar,par)
        
main()