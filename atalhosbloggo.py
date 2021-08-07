def trocarSub(v):
    aux = True 
    i = 0
    while i < len(v):
        if v[i] == "_" and aux:
            v[i] ="<" 
            v.insert(i+1,"i")
            v.insert(i+2,">")
            aux = False
        elif v[i] == "_" and aux == False:
            v[i] ="<" 
            v.insert(i+1,"/")
            v.insert(i+2,"i")
            v.insert(i+3,">")
            aux = True
        i+=1

#------------------------------------------------

def trocarBold(v):
    aux = True
    i = 0 
    while i<len(v):
        if v[i] == "*" and aux:
            v[i] ="<" 
            v.insert(i+1,"b")
            v.insert(i+2,">")
            aux = False
        elif v[i] == "*" and aux == False:
            v[i] ="<" 
            v.insert(i+1,"/")
            v.insert(i+2,"b")
            v.insert(i+3,">")
            aux = True
        i+=1    

#----------------------------------------------------

def main():
    while True:
        try:
            text = list(input())
            trocarSub(text)
            trocarBold(text)
            print("".join(text))
        except EOFError:
            break
main()