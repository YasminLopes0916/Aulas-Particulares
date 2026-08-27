#Exercicio11
print("Boa noite, eu sou o Dr Sheppard! Estou ajudando o Monsieur Poirot com a investigação. Fiquei responsável pela coleta dos depoimentos. Vamos começar?")
nome_do_suspeito = input("Primeiramente, qual é o seu nome? ")
horario_visto_ultima_vez = int(input("Que horas você foi visto em público pela última vez: antes das 20h, entre 20h e 22h ou depois das 22h? "))
alibi = str(input("Você possui um álibi? Alguém que confirme essa informação sobre o seu horário, sim ou não? ")).lower().strip()
if horario_visto_ultima_vez < 20:
    print(f"Certo, {nome_do_suspeito}. Então nossa suspeita é baixa.")
    if alibi == "sim":
        print("Álibi confirmado. Você está liberado(a). Obrigado pelo seu depoimento!")
    else:
        print("Sem álibi. Suspeita mantida em nível baixo! Você continuará sendo investigado(a).")
elif 20 <= horario_visto_ultima_vez <= 22:
    print(f"Certo, {nome_do_suspeito}. Então nossa suspeita é moderada.")
    if alibi == "sim":
        print("Álibi confirmado. Nível de suspeita reduzido para baixo! Porém, você continuará sendo investigado(a)")
    else:
        print("Sem álibi. Você será conduzido para a delegacia!")
elif horario_visto_ultima_vez > 22:
    print(f"Certo, {nome_do_suspeito}. Então nossa suspeita é alta")
    if alibi == "sim":
        print("Álibi confirmado. Suspeita reduzida para moderada! Porém, você continuará sendo investigado(a)")
    else: 
        print("Sem álibi. Você será conduzido para a delegacia!!!")
#Não se esquecer de colocar respostas mais objetivas, dar uma conclusão. 