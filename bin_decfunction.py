def binDec(n):
    i = 0
    mod = 0
    dec = 0
    while n != 0:
        n = n // 10
        mod = n % 10
        dec = dec + mod * 2 ** i
        i+=1

    return print(dec)

def main():
    dec = int(input())
    binDec(dec)

main()