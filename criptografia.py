def deslocaTres(msg):
    for i in range(0,len(msg)):
        if 64<ord(msg[i])<90 or 96<ord(msg[i])<123:
            msg[i] = ord(msg[i]) + 3
            msg[i] = chr(msg[i])
    return msg

#------------------------------------------------------------

def inverter(d):
    j = len(d)-1
    inv = [0] * len(d)
    for i in range(0,len(d)):
        inv[j] = d[i]
        d[i] = inv[j]
        j-=1
    return inv

#------------------------------------------------------------

def deslocaMet(inv):
    for i in range(len(inv)//2, len(inv)):
        inv[i] = ord(inv[i]) -1
        inv[i] = chr(inv[i])
    return inv

    
#------------------------------------------------------------

def main():
    t = int(input())
    for i in range(0,t):
        mensagem = list(input())
        cripto = deslocaMet(inverter(deslocaTres(mensagem)))
        cripto = "".join(cripto)
        print(f"{cripto}")

main()