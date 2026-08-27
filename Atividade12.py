#Exercicio12
nome_do_suspeito = str(input("Primeiramente, qual é o seu nome? "))
relacao_vitima = str(input("Qual era a sua relação com Roger Ackroyd? Selecione apenas uma opção: parente, empregado, amigo ou desconhecido? ")).lower().strip()
heranca = str(input("Você foi contemplado no testamento de Roger Ackrouyd, sim ou não? ")).lower().strip()
if heranca == "sim":
    valor_heranca = float(input(f"Entendo, {nome_do_suspeito}. E quanto você herdaria em dinheiro? "))
hora_crime = input("Responda com sim ou não. Você estava na mansão na hora do crime? ").lower().strip()
if heranca == "sim":
    print("Como você tem herança. Vamos avaliar outras variáveis do caso!")
    if hora_crime == "sim":
        print("Nesse caso, como você tem herança e estava na mansão no dia crime, então você é um suspeito prioritário!")
    else:
        print("Nesse caso, como você tem herança e não estava na mansão no dia crime, então você é um suspeito secundário!")
else:
    print("Como você não tem herança. Vamos avaliar outras variáveis do caso!")
    if hora_crime == "sim":
        print("Nesse caso, como você não tem herança, mas estava na mansão no dia crime, então você é um suspeito secundário!")
    else:
        print("Nesse caso, como você não tem herança e não estava na mansão no dia crime, então estamos sem indícios suficientes!")
#input já traz como srt!