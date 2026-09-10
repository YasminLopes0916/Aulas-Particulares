#Exercicio14
nome = input("Nome do suspeito: ")
relacao = input("Relação com a vítima (familiar, empregado, sócio, desconhecido): ")
alibi = input("Possui álibi confirmado por terceiros? (sim/não): ")
heranca = float(input("Quantia que herdaria/lucraria com a morte da vítima, em reais: "))
visto_cena = input("Foi visto próximo à cena do crime no horário do óbito? (sim/não): ")
if relacao == "familiar":
    if alibi == "não":
        if heranca < 10000:
            print(f"{nome} (familiar): suspeito fraco - motivo financeiro baixo e sem álibi.")
        elif heranca <= 100000:
            print(f"{nome} (familiar): suspeito relevante - motivo financeiro moderado e sem álibi.")
        else:
            if visto_cena == "sim":
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
        elif heranca <= 100000:
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
        elif heranca <= 100000:
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
        elif heranca <= 100000:
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