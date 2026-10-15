import random
numero = 0 #não era necessário colocar ele, só se ele fosse uma var do while, que seria criada após o while.
informante = input("Sou o detetive John Sugar. Obrigado por contribuir com o caso. Qual é o seu nome? ")
pista = input("Que pista é essa: uma testemunha, um documento, uma gravação ou um rastreamento? ")
palpite = int(input("Sobre a credibilidade da pista. De 0 a 10, quanto Sugar acredita na veracidade dela? "))
while palpite < 0 or palpite > 10:
    palpite = int(input("Valor inválido. Digite um número de 0 a 10: "))
hora_pista = random.randint(1, 48)
pista_verificada = random.randint(0, 10)
print("\n--- Resultado do laboratório ---")
print("Informante:", informante)
print("Tipo de pista:", pista)
print("Horas desde a obtenção da pista:", hora_pista)
print("Credibilidade real (laboratório):", pista_verificada)
print("Palpite de Sugar:", palpite)
print("--------------------------------\n")
if pista == "testemunha":
    if hora_pista < 12 and pista_verificada >= 7:
        print("Prioridade máxima")
        if palpite >= 7:
            print("Intuição e laboratório concordam, agir imediatamente")
        else:
            print("A intuição de Sugar diverge do laboratório, revisar antes de agir")
    else:
        print("Prioridade baixa")
        if hora_pista > 36 or pista_verificada < 3:
            print("Descartar pista")
elif pista == "documento":
    if hora_pista < 12 and pista_verificada >= 7:
        print("Prioridade máxima")
        if palpite >= 7:
            print("Intuição e laboratório concordam, agir imediatamente")
        else:
            print("A intuição de Sugar diverge do laboratório, revisar antes de agir")
    else:
        print("Prioridade baixa")
        if hora_pista > 36 or pista_verificada < 3:
            print("Descartar pista")
elif pista == "gravação":
    if hora_pista < 12 and pista_verificada >= 7:
        print("Prioridade máxima")
        if palpite >= 7:
            print("Intuição e laboratório concordam, agir imediatamente")
        else:
            print("A intuição de Sugar diverge do laboratório, revisar antes de agir")
    else:
        print("Prioridade baixa")
        if hora_pista > 36 or pista_verificada < 3:
            print("Descartar pista")
elif pista == "rastreamento": #esse else era pra ser caso o user digitasse errado. A seq. correta deveria ser: if, elif, elif, elif e else.
    if hora_pista < 12 and pista_verificada >= 7:
        print("Prioridade máxima")
        if palpite >= 7:
            print("Intuição e laboratório concordam, agir imediatamente")
        else:
            print("A intuição de Sugar diverge do laboratório, revisar antes de agir")
    else:
        print("Prioridade baixa")
        if hora_pista > 36 or pista_verificada < 3:
            print("Descartar pista")
else:
    print("Pista inválida!")