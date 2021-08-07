def minimiza(t):
    for i in range(len(t)):
        n = ord(t[i])
        if 64<n<91:
            n += 32
            t[i] = chr(n)
#---------------------------------------------

def verAliteracao(t):
    verif = ord(t[0]) 
    aliteracao = 0
    aux = 0 
    for i in range(1,len(t)):
        snum = ord(t[i])
        if snum == 32 and verif == ord(t[i+1]) and aux != verif:
            aliteracao += 1
            aux = verif
        elif snum == 32 and i+1<len(t) and verif != ord(t[i+1]):
            verif = ord(t[i+1])
            aux = 0
    return aliteracao

#----------------------------------------------

def main():
    while True:
        try:
            text = list(input())
            minimiza(text)
            print(verAliteracao(text))
        except EOFError:
            break
main()