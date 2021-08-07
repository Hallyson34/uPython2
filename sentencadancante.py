def funcDancante(txt):
    alterna = True
    for i in range(len(txt)):
        nums = ord(txt[i]) 
        if alterna and nums != 32:
            alterna = False
            if nums > 90:
                nums -= 32
                alterna = False
        elif alterna == False and 64<nums<91:
            nums += 32
            alterna = True
        elif nums != 32:
            alterna = True
        txt[i] = chr(nums)
    return txt            

#----------------------------------------

def main():
    while True:
        try:
            text = list(input())
            stext = "".join(funcDancante(text))
            print(stext)
        except EOFError:
            break
main()