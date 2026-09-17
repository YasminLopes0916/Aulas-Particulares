idade = int(input("Qual é a sua idade? "))
ingresso = input("Você tem o igresso do evento? (sim/não): ")
lista_vip = input("Você está na lista vip? (sim/não): ")
if idade < 12:
    print ("Você tem idade menor que 12 anos, por isso não pode entrar no evento!")
elif idade >= 18 and (ingresso == "sim" or lista_vip == "sim"):
    print("Sua entrada é permitida!")
elif idade < 18 and (ingresso == "sim" or lista_vip == "sim"):
    autorizacao = input("Você tem a autorização dos seus pais para participar do evento? (sim/não): ")
    if autorizacao == "sim":
        print("Você pode entrar, pois tem a autorização e o ingresso do evento!")
    else: #mais eficiente que ficar colocando comando pra barrar erro de digitacao
        print("Você não pode entrar, pois apesar de ter o ingresso não está com a autorização dos seus responsáveis.")
else:
    print("Então sua entrada não é permitida!")

""""Vamos criar um sistema de controle de entrada para um evento! As Regras são:
A entrada é permitida se a pessoa tem idade maior ou igual a 18 anos e tem ingresso.
Se a pessoa tem menos de 18 anos, só pode entrar com autorização dos pais e ingresso.
Pessoas com idade menor que 12 anos não podem entrar de jeito nenhum
Se a pessoa disser que está na lista VIP, pode entrar mesmo sem ingresso.
Caso contrário, a entrada deve ser negada."""

#Cuidardaordem: do mais simples pro mais complexo -> boas práticas
#ingresso == "sim" or lista_vip == "sim" isso é correto, agora isso está completamente errado ingresso or lista_vip == "sim". Qusando coloco so 1 var sem comparacao
#o codigo vai testar se tem algo dentro da variavel e se tiver ele retorna true, mesmo q esteja "errado".
#muitooo cuidado com a estrutura ser especifica