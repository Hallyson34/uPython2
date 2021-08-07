def combinar(vet1, vet2):
    vet3 = []
    if len(vet2)>len(vet1):
        for i in range(0,len(vet1)):
            vet3 += vet1[i] + vet2[i]
        vet3 += vet2[len(vet1):len(vet2)]
        return "".join(vet3)
    else:
        for i in range(0,len(vet2)):
            vet3 += vet1[i] + vet2[i]
        vet3 += vet1[len(vet2):len(vet1)]
        return "".join(vet3)

#-----------------------------------------------

def main():
    t = int(input())
    for i in range (0,t):
        v1, v2 = list(map(str, input().split()))
        print(combinar(v1, v2))
main()