#Exercicio19
idade = int(input("Qual é a sua idade? "))
experiencia = input("Você possui experiência na área: sim ou não? ")
educacao = input("Você possui graduação: sim ou não? ")
criminais = input("Você possui antecedentes criminais: sim ou não? ")
indicaçao = input("Você possui referência/indicação de alguém interno à empresa: sim ou não? ")
if (idade > 18) and (experiencia == "sim") and (not criminais == "sim"):
    print("Excelente! Você será chamado para uma entrevista!")
elif (educacao == "sim" or indicaçao == "sim") and (not criminais == "sim"):
    print("Excelente! Você será chamado para uma entrevista!")
else:
    print("Agradecemos pela sua participação, mas seu perfil não atende nossas necessidades no momento.")


# not criminais é possível usar o not pra inverter uma variavel
#respeitar sempre a lógica de negócios: fazer o um programa alinhado ao que o cliente exige, pois ele entende mais da realidade do negócio que o programador.
#não esquecer das aspas dentro dos ifs (experiencia == "não") não e sim tem que ter "" pois são strings.
#nunca esquecer de isolar os or usando os () dos and, senão o programa executa mesmo com a condição do and sendo falsa. Assim garantimos a prioridade do and. 
"""Vamos desenvolver um sistema para avaliar candidatos para uma vaga de emprego. O candidato só será contratado se:
Tem mais de 18 anos e Tem experiência na área e
Não possui antecedentes criminais
Se o candidato não tem experiência, mas tem pelo menos ensino superior completo ou foi indicado por alguém da empresa e não tem antecedentes então
 será chamado para uma entrevista.
Em todos os outros casos, o candidato será rejeitado."""