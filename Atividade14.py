#Exercicio14
nome = input("Nome do suspeito: ").lower().strip()
relacao = input("Relação com a vítima (familiar, empregado, sócio, desconhecido): ").lower().strip()
alibi = input("Possui álibi confirmado por terceiros? (sim/não): ").lower().strip()
heranca = float(input("Quantia que herdaria/lucraria com a morte da vítima, em reais: "))
visto_cena = input("Foi visto próximo à cena do crime no horário do óbito? (sim/não): ").lower().strip()
nível_de_suspeita = 0
if relacao == "familiar":
    nível_de_suspeita += 3 #print em seguida
    if alibi == "não":
        nível_de_suspeita += 5 #print em seguida
        if heranca < 10000:
            print(f"{nome} (familiar): suspeito fraco - motivo financeiro baixo e sem álibi.")
        elif heranca < 100000:
            print(f"{nome} (familiar): suspeito relevante - motivo financeiro moderado e sem álibi.")
        else:
            nível_de_suspeita += 5 #print em seguida (da herança!!)
            if visto_cena == "sim":
                nível_de_suspeita += 10 #print em seguida:
                print(f"Nível de suspeita = {níyasminvel_de_suspeita}")
                print(f"{nome} (familiar): SUSPEITO NÚMERO UM - motivo financeiro alto, sem álibi e visto na cena.")
            else:
                print(f"{nome} (familiar): suspeito relevante - motivo financeiro alto, mas não foi visto na cena.")
    else:
        if visto_cena == "sim":
            print(f"{nome} (familiar): suspeito relevante - álibi confirmado, mas foi visto na cena (contradição a investigar).")
        else:
            print(f"{nome} (familiar): provavelmente inocente - álibi confirmado e não visto na cena.")
elif relacao == "empregado":
    if alibi == "não":
        if heranca < 10000:
            print(f"{nome} (empregado): suspeito fraco - motivo financeiro baixo e sem álibi.")
        elif heranca < 100000:
            print(f"{nome} (empregado): suspeito relevante - motivo financeiro moderado e sem álibi.")
        else:
            if visto_cena == "sim":
                print(f"{nome} (empregado): SUSPEITO NÚMERO UM - motivo financeiro alto, sem álibi e visto na cena.")
            else:
                print(f"{nome} (empregado): suspeito relevante - motivo financeiro alto, mas não foi visto na cena.")
    else:
        if visto_cena == "sim":
            print(f"{nome} (empregado): suspeito relevante - álibi confirmado, mas foi visto na cena (contradição a investigar).")
        else:
            print(f"{nome} (empregado): provavelmente inocente - álibi confirmado e não visto na cena.")
elif relacao == "sócio":
    if alibi == "não":
        if heranca < 10000:
            print(f"{nome} (sócio): suspeito fraco - motivo financeiro baixo e sem álibi.")
        elif heranca < 100000:
            print(f"{nome} (sócio): suspeito relevante - motivo financeiro moderado e sem álibi.")
        else:
            if visto_cena == "sim":
                print(f"{nome} (sócio): SUSPEITO NÚMERO UM - motivo financeiro alto, sem álibi e visto na cena.")
            else:
                print(f"{nome} (sócio): suspeito relevante - motivo financeiro alto, mas não foi visto na cena.")
    else:
        if visto_cena == "sim":
            print(f"{nome} (sócio): suspeito relevante - álibi confirmado, mas foi visto na cena (contradição a investigar).")
        else:
            print(f"{nome} (sócio): provavelmente inocente - álibi confirmado e não visto na cena.")
elif relacao == "desconhecido":
    if alibi == "não":
        if heranca < 10000:
            print(f"{nome} (desconhecido): suspeito fraco - motivo financeiro baixo e sem álibi.")
        elif heranca < 100000:
            print(f"{nome} (desconhecido): suspeito relevante - motivo financeiro moderado e sem álibi.")
        else:
            if visto_cena == "sim":
                print(f"{nome} (desconhecido): SUSPEITO NÚMERO UM - motivo financeiro alto, sem álibi e visto na cena.")
            else:
                print(f"{nome} (desconhecido): suspeito relevante - motivo financeiro alto, mas não foi visto na cena.")
    else:
        if visto_cena == "sim":
            print(f"{nome} (desconhecido): suspeito relevante - álibi confirmado, mas foi visto na cena (contradição a investigar).")
        else:
            print(f"{nome} (desconhecido): provavelmente inocente - álibi confirmado e não visto na cena.")
else:
    print("Relação com a vítima não reconhecida pela investigação.")

#Erros/ajustes: não coloquei em else do álibi = NÃO, um teste de verificação da herança e nem o visto em cena. 
#No álibi = SIM, coloquei a herança, mas coloquei o visto em cena somente no else. Ficou faltando no If e Elif
#Ficou faltando implementar esses ajustes em cada uma das categorias: socio, desconhecido e empregado.
#Continuar colocando print em TODAS as camadas. Porém, só dizer o tipo de suspeito na última camada (que nesse caso era a quarta).
#Pra indicar se um suspeito é fraco, forte ou inocente - use um nível de suspeita do menor para o maior - como em: provavelmente inocente; suspeito fraco; suspeito relevante; SUSPEITO NÚMERO UM.
#Desafio extra: Colocar print em TODAS as camadas! Dando um feedback - mas sem spoiler - só revelar no final - ultima camada/suspeito.
#Refazer as 4 camadas com 48 casos.
#Atribuir novos pesos em cada requisito. Exemplo: para cada categoria de relação (familiar, sócio, etc) atribuir uma escala de peso a depender do tipo de relação.
#Colocar no próprio código o cálculo de nível de suspeita: Numero 1 = 23 - Parentesco: 0,1,2,3 - Alibi: 0,5 - Herança: 0,3,5 - Visto: 0,10.
#Colocar as variáveis dentro dos Ifs.