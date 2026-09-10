#Exercicio15
nome = input("Olá! Sou o detetive Hércule Poiroit e estou investigando o assassinato de Ackroyd. Primeiramente, qual é o seu nome? ").lower().strip()
relacao = input("Sua relação com Ackroyd: de familiar, empregado, sócio ou desconhecido? ").lower().strip() #nivel_de_suspeita:0-3
alibi = input("Você possui álibi confirmado por terceiros, sim ou não? ").lower().strip() #nivel_de_suspeita:0_ou_5
visto_cena = input("Você foi visto próximo à cena do crime no horário do óbito, sim ou não? ").lower().strip() #nivel_de_suspeita:0_ou_10
heranca = float(input("Qual o valor do montante da sua herança em reais? ")) #nivel_de_suspeita:0(pra=>100.000)_3(pra=>1.000.000)_ou_5(pra>=1.000.000.000)
nivel_de_suspeita = 0 #Obs: o suspeito nº1 deve atingir 23 pontos!
 
if relacao == "familiar":
    nivel_de_suspeita += 3
    print("Uh! Vocês eram parentes?! Sendo assim, você herdaria alguma coisa de Ackroyd.")
    if alibi == "não":
        nivel_de_suspeita += 5
        print("Então quer dizer que você NÃO tem álibi.")
        if heranca <= 100000:
            nivel_de_suspeita += 0
            print("O valor da herança envolvida é relativamente baixo.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        elif heranca <= 1000000:
            nivel_de_suspeita += 3
            print("O valor da herança já chama mais atenção.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        else: #o ideal mesmo seria um ELIF pra diferencia entre 1 milhao e 1 bilhao!!!
            nivel_de_suspeita += 5 
            print("Mon ami, que situação delicada! Estamos falando de uma fortuna considerável.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
    else:
        nivel_de_suspeita += 0
        print("Uh! Melhor pra você. Então você tem um álibi.")
        if heranca <= 100000:
            nivel_de_suspeita += 0
            print("O valor da herança envolvida é relativamente baixo.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        elif heranca <= 1000000:
            nivel_de_suspeita += 3
            print("O valor da herança já chama mais atenção.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        else:
            nivel_de_suspeita += 5
            print("Mon ami, que situação delicada! Estamos falando de uma fortuna considerável.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
elif relacao == "sócio":
    nivel_de_suspeita += 2
    print("Sócio da vítima... interesses financeiros em comum costumam pesar numa investigação.")
    if alibi == "não":
        nivel_de_suspeita += 5
        print("Então quer dizer que você NÃO tem álibi.")
        if heranca <= 100000:
            nivel_de_suspeita += 0
            print("O valor da herança envolvida é relativamente baixo.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        elif heranca <= 1000000:
            nivel_de_suspeita += 3
            print("O valor da herança já chama mais atenção.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        else:
            nivel_de_suspeita += 5
            print("Mon ami, que situação delicada! Estamos falando de uma fortuna considerável.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
    else:
        nivel_de_suspeita += 0
        print("Uh! Melhor pra você. Então você tem um álibi.")
        if heranca <= 100000:
            nivel_de_suspeita += 0
            print("O valor da herança envolvida é relativamente baixo.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        elif heranca <= 1000000:
            nivel_de_suspeita += 3
            print("O valor da herança já chama mais atenção.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        else:
            nivel_de_suspeita += 5
            print("Mon ami, que situação delicada! Estamos falando de uma fortuna considerável.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
elif relacao == "empregado":
    nivel_de_suspeita += 1
    print("Empregado de Ackroyd. Vale entender melhor essa relação de trabalho.")
    if alibi == "não":
        nivel_de_suspeita += 5
        print("Então quer dizer que você NÃO tem álibi.")
        if heranca <= 100000:
            nivel_de_suspeita += 0
            print("O valor da herança envolvida é relativamente baixo.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        elif heranca <= 1000000:
            nivel_de_suspeita += 3
            print("O valor da herança já chama mais atenção.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        else:
            nivel_de_suspeita += 5
            print("Mon ami, que situação delicada! Estamos falando de uma fortuna considerável.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
    else:
        nivel_de_suspeita += 0
        print("Uh! Melhor pra você. Então você tem um álibi.")
        if heranca <= 100000:
            nivel_de_suspeita += 0
            print("O valor da herança envolvida é relativamente baixo.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        elif heranca <= 1000000:
            nivel_de_suspeita += 3
            print("O valor da herança já chama mais atenção.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        else:
            nivel_de_suspeita += 5
            print("Mon ami, que situação delicada! Estamos falando de uma fortuna considerável.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
else:
    nivel_de_suspeita += 0
    print("Você diz não ter relação nenhuma com Ackroyd. Interessante...")
    if alibi == "não":
        nivel_de_suspeita += 5
        print("Então quer dizer que você NÃO tem álibi.")
        if heranca <= 100000:
            nivel_de_suspeita += 0
            print("O valor da herança envolvida é relativamente baixo.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        elif heranca <= 1000000:
            nivel_de_suspeita += 3
            print("O valor da herança já chama mais atenção.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        else:
            nivel_de_suspeita += 5
            print("Mon ami, que situação delicada! Estamos falando de uma fortuna considerável.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
    else:
        nivel_de_suspeita += 0
        print("Uh! Melhor pra você. Então você tem um álibi.")
        if heranca <= 100000:
            nivel_de_suspeita += 0
            print("O valor da herança envolvida é relativamente baixo.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        elif heranca <= 1000000:
            nivel_de_suspeita += 3
            print("O valor da herança já chama mais atenção.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
        else:
            nivel_de_suspeita += 5
            print("Mon ami, que situação delicada! Estamos falando de uma fortuna considerável.")
            if visto_cena == "sim":
                nivel_de_suspeita += 10
                print("Você foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")
               
            else:
                nivel_de_suspeita += 0
                print("Você não foi visto próximo à cena do crime no horário do óbito.")
                print(f"Nível de suspeita = {nivel_de_suspeita}")

if nivel_de_suspeita <= 5:
    print(f"{nome} ({relacao}): provavelmente inocente.")
elif nivel_de_suspeita <= 12:
    print(f"{nome} ({relacao}): suspeito fraco.")
elif nivel_de_suspeita <= 19:
     print(f"{nome} ({relacao}): suspeito relevante.")
elif nivel_de_suspeita < 23:
    print(f"{nome} ({relacao}): suspeito forte.")
else:
    print(f"{nome} ({relacao}): SUSPEITO NÚMERO UM.")
#Colocar no próprio código o cálculo de nível de suspeita: Numero 1 = 23 - Parentesco: 0,1,2,3 - Alibi: 0,5 - Herança: 0,3,5 - Visto: 0,10.
#Colocar as variáveis dentro dos Ifs.
#Da próxima vez seja mais sucinta no código, sem repetir várias estruturas repetitivas.
#Tomar cuidado com as sequências corretas/otimizadas de condicionais.
"""Não precisa esmiuçar tantos if, elif, elif, else, pro print da pontuação - como a 5° camada da árvore -
não precisa colocar a estrutura no final de cada decisão, colocando ele uma vez depois da árvore inteira 
já vai ter o mesmo resultado - economizando 480 linhas"""
