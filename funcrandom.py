import random
def rand():
    u=0
    while u<10:
        x = random.randint(1,6)
        print(f"{x}", end=" ")
        u+=1
rand()