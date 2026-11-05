import random
confianca = 0 #esse valor só serve pra iniciar o while, depois ele será substituído
while confianca < 5:
    nome = input("Nome do agente: ") 
    confianca = random.randint(1,10) #var retomada pra gerar o valor aleatório
    print(f"O valor da confiança é de: {confianca}.")
    if confianca >= 5:
        print(f"Lecter confia em {nome}. Podemos prosseguir com o inquérito.")
    else:
        print(f"Lecter não confia em {nome}. Tente outro agente para prosseguir com o inquérito.")
rodada = 1
pistas = 0
lista_assuntos = ["familia", "caso", "passado", "cela"]
while rodada < 5 and pistas < 3:
    assunto = input(f"Assunto ({lista_assuntos}): ")
    assunto = assunto.strip().lower()
    while assunto not in lista_assuntos: #usando o in ele filtra o item na lista isso otimiza o código
        assunto = input("Assunto invalido! Digite familia, caso, passado ou cela: ")
        assunto = assunto.strip().lower()
    humor = random.randint(1, 10)
    print("Humor do Lecter: ", humor)
    if assunto == "familia":
        lista_assuntos[0] = "" #transformando o item em nada
        if humor >= 7 and confianca >= 6:
            print("Lecter revela uma pista!")
            pistas = pistas + 1
            if humor == 10:
                print("Humor 10! Pista extra!")
                pistas = pistas + 1
        else:
            print("Lecter se recusa a responder.")
            if humor <= 3:
                print(f"{nome} perde confianca.")
                confianca = confianca - 1
    elif assunto == "caso":
        lista_assuntos[1] = "" #transformando o item em nada
        if humor >= 6 and confianca >= 5:
            print("Lecter revela uma pista!")
            pistas = pistas + 1
            if humor == 10:
                print("Humor 10! Pista extra!")
                pistas = pistas + 1
        else:
            print("Lecter se recusa a responder.")
            if humor <= 3:
                print(f"{nome} perde confianca.")
                confianca = confianca - 1
    elif assunto == "passado":
        lista_assuntos[2] = "" #transformando o item em nada
        if humor >= 8 and confianca >= 7:
            print("Lecter revela uma pista!")
            pistas = pistas + 1
            if humor == 10:
                print("Humor 10! Pista extra!")
                pistas = pistas + 1
        else:
            print("Lecter se recusa a responder.")
            if humor <= 3:
                print(f"{nome} perde confianca.")
                confianca = confianca - 1
    elif assunto == "cela":
        lista_assuntos[3] = "" #transformando o item em nada
        if humor >= 5 and confianca >= 4:
            print("Lecter revela uma pista!")
            pistas = pistas + 1
            if humor == 10:
                print("Humor 10! Pista extra!")
                pistas = pistas + 1
        else:
            print("Lecter se recusa a responder.")
            if humor <= 3:
                print(f"{nome} perde confianca.")
                confianca = confianca - 1
    print("Fim da rodada", rodada, "- Pistas:", pistas, "- Confianca:", confianca, "\n") #"\n" usa para pular uma linha. Assim não precisa colocar o print vazio
    rodada = rodada + 1
if pistas >= 3:
    print("Agente", nome, "conseguiu pistas suficientes!")
elif pistas >= 1:
    print("Agente", nome, "conseguiu algumas pistas, mas nao o suficiente.")
else:
    print("Agente", nome, "nao conseguiu nenhuma pista.")