def main():
    vet = []

    for i in range(0,10):
        num = int(input())
        vet.append(num)  
        if vet[i] <= 0:
            print(f"x[{i}] = 1")
        else:
            print(f"x[{i}] = {vet[i]}")

main()