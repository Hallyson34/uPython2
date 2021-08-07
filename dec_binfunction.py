def decBin(n):
    i = 0
    mod = 0
    binario = 0
    while n !=0:
        mod = n % 2
        n = n // 2
        binario += mod * 10 ** i
        i+=1
    
    return print(binario)
def main():
    dec = int(input())
    decBin(dec)

main()