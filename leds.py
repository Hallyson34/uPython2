def contarLed(n):  
    led = 0
    for i in range(0,len(n)):
        if n[i] == "2" or n[i] == "3" or n[i] == "5":
            led += 5
        elif n[i] == "6" or n[i] == "9" or n[i] == "0":
            led += 6
        elif n[i] == "4":
            led += 4
        elif n[i] == "1":
            led += 2
        elif n[i] == "8":
            led += 7
        else:
            led += 3
    return led

#-----------------------------------------------

def main():
    t = int(input())
    for i in range(0,t):
        num = list(input())
        print(f"{contarLed(num)} leds")

main()