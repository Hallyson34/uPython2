def decodifica(txt,num):
    for i in range(len(txt)):
        txt[i] = ord(txt[i]) - num
        if txt[i]<65:
            txt[i] += 26
        txt[i] = chr(txt[i])
    return txt

#-----------------------------

def main():
    t = int(input())
    for i in range(t):
        text = list(input())
        n = int(input())
        stext = "".join(decodifica(text,n))
        print(stext)

main()