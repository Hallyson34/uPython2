def calcFib(num):
    vet = [0, 1]
    for i in range(2,num+1):
        vet.append(vet[i-1]+vet[i-2])
    return vet[num]
#--------------------------------------------------
def main():
    t = int(input())
    for i in range(0,t):
        n = int(input())
        print(f"Fib({n}) = {calcFib(n)}")
        
main()
    

    