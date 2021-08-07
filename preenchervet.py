def main():
    n = int(input())
    vet = []
    for i in range(0,10):
        vet.append(n)
        print(f"N[{i}] = {vet[i]}")
        n = n + n

main()
