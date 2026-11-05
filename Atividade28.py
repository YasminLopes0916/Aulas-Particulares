import random
import time
nome = input("Digite o nome da personagem: ")
noite = 1
cansaco = 0
while noite <= 5 and cansaco < 10:
    barulho = random.randint(1, 10)
    print(f"Noite {noite} - barulho: {barulho} - cansaco: {cansaco} ")

    if barulho <= 3:
        print("Rosemary dorme bem")
    elif barulho <= 7:
        print("Rosemary dorme mal")
        cansaco += 2
    else:
        print("Rosemary não dorme")
        cansaco += 4
    noite += 1
    time.sleep(2)
print(f"Cansaco final: {cansaco} ")
if cansaco >= 10:
    print(f"{nome} desistiu de dormir e fez o pacto!")
else:
    print(f"{nome} aguentou as 5 noites e ficou com Jesus!")
"""Para o programa retornar cada print lentamente, use a biblioteca time e a função sleep. Devo colocar a função sleep antes
do print e depois dos if, elif, else. 