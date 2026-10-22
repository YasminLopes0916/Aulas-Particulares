import random
nome = input("Nome do hóspede: ")
tipo = input("Tipo de quarto (standard/superior/suíte/suíte presidencial): ")
orcamento = float(input("Orçamento por noite: "))
noites = int(input("Número de noites: "))
while noites < 1 or noites > 30:
    noites = int(input("Número de noites inválido (1 a 30). Digite novamente: "))
ocupacao = random.randint(30, 100)
lobby_boys = random.randint(0, 5)
print(f"\nOcupação do hotel: {ocupacao}%")
print(f"Lobby Boys disponíveis: {lobby_boys}\n")
if tipo == "standard":
    preco = 100
    print(f"Custo total : {preco * noites}")
    if orcamento >= preco * noites and ocupacao < 90: #deveria ter colocado - além da ocupação o cálculo de multiplicação
        print(f"Reserva confirmada para {nome}!")
        if noites >= 7 and lobby_boys >= 1:
            print("Recepção especial com carregamento de malas.")
        else:
            print("Check-in padrão.")
    else:
        if ocupacao >= 90 or lobby_boys == 0:
            print(f"Desculpe, {nome}. Hotel lotado, lista de espera.")
        else:
            falta = preco * noites - orcamento #diferente da calculadora o pyhton identifica a prioridade de operação
            print(f"Desculpe, {nome}. Orçamento insuficiente, sugerir um quarto mais simples.")
            print(f"Faltam R$ {falta/noites :.2f} por noite (R$ {falta:.2f} no total).")
elif tipo == "superior":
    preco = 200
    print(f"Custo total : {preco * noites}")
    if orcamento >= preco * noites and ocupacao < 90:
        print(f"Reserva confirmada para {nome}!")
        if noites >= 7 and lobby_boys >= 1:
            print("Recepção especial com carregamento de malas.")
        else:
            print("Check-in padrão.")
    else:
        if ocupacao >= 90 or lobby_boys == 0:
            print(f"Desculpe, {nome}. Hotel lotado, lista de espera.")
        else:
            falta = preco * noites - orcamento #diferente da calculadora o pyhton identifica a prioridade de operação
            print(f"Desculpe, {nome}. Orçamento insuficiente, sugerir um quarto mais simples.")
            print(f"Faltam R$ {falta/noites :.2f} por noite (R$ {falta:.2f} no total).")
elif tipo == "suíte":
    preco = 400
    print(f"Custo total : {preco * noites}")
    if orcamento >= preco * noites and ocupacao < 90:
        print(f"Reserva confirmada para {nome}!")
        if noites >= 7 and lobby_boys >= 1:
            print("Recepção especial com carregamento de malas.")
        else:
            print("Check-in padrão.")
    else:
        if ocupacao >= 90 or lobby_boys == 0:
            print(f"Desculpe, {nome}. Hotel lotado, lista de espera.")
        else:
            falta = preco * noites - orcamento #diferente da calculadora o pyhton identifica a prioridade de operação
            print(f"Desculpe, {nome}. Orçamento insuficiente, sugerir um quarto mais simples.")
            print(f"Faltam R$ {falta/noites :.2f} por noite (R$ {falta:.2f} no total).")
elif tipo == "suíte presidencial":
    preco = 800
    print(f"Custo total : {preco * noites}")
    if orcamento >= preco * noites and ocupacao < 90:
        print(f"Reserva confirmada para {nome}!")
        if noites >= 7 and lobby_boys >= 1:
            print("Recepção especial com carregamento de malas.")
        else:
            print("Check-in padrão.")
    else:
        if ocupacao >= 90 or lobby_boys == 0:
            print(f"Desculpe, {nome}. Hotel lotado, lista de espera.")
        else:
            falta = preco * noites - orcamento #diferente da calculadora o pyhton identifica a prioridade de operação
            print(f"Desculpe, {nome}. Orçamento insuficiente, sugerir um quarto mais simples.")
            print(f"Faltam R$ {falta/noites :.2f} por noite (R$ {falta:.2f} no total).")
else:
    print("Tipo de quarto desconhecido.")