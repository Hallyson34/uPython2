def ordena(v):
    for j in range(1, len(v)):
        pivo = v[j]
        i = j - 1
        while v[i] > pivo and i >=0:
            v[i+1] = v[i]
            i = i - 1

        v[i+1] = pivo


def main():
    v = list(map(int, input().split()))
    print(v)
    ordena(v)
    print(v)

main()