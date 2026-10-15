import random
numero = 0 #variável necessária antes de colocar o while
maximo = int(input("Vamos apostar! Você quer adivinhar um número de 1 até quanto? "))
chances = int(input("Quantas chances você deseja ter para conseguir acertar o número secreto? "))
secreto = random.randint(1,maximo) #onde começa e termina os valores a serem escolhidos
while numero != secreto and chances != 0: #While para de repetir pq o user acertou o numero secreto ou acabou suas chances
    numero = int(input(f"Tente advinhar um número entre 1 e {maximo}: "))
    if numero < secreto:
        print(f"Tente um número maior que {numero}.")
    elif numero == secreto:
        print(f"Parabéns! Você acertou o número secreto que é o: {numero}!")
    elif numero > secreto:
        print(f"Tente um número menor que {numero}.")
    chances -= 1
    print(f"Você tem {chances} chances.")
if  numero != secreto and chances == 0:
    print("Você perdeu! Suas chances acabaram!")


#Cuidado com a ordem, sempre colocar a variável antes do comando.
#chances -= 1 é o oposto da atividade do rainfall
#Tirar a condicional da indentação do loop - e especificar que é porque as chances acabaram - faz com que ela seja executada depois que o loop acabar.