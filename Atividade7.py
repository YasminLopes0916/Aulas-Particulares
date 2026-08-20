#Exercicio7
idade = int(input("Informe qual é a sua idade? "))
dinheiro = input("Informe quantos reais você tem? ")
correcao_virgula = dinheiro.replace("," , ".")
dinheiro = float(correcao_virgula)
if idade < 15:
    print("Como você tem menos de 15 anos, sua compra terá um desconto e custará apenas R$ 45.")
    if dinheiro >= 45:
        print("Parabéns pela compra!")
    else: 
        print("Valor insuficiente. Você precisa de R$ 45 para realizar a compra.")
else:
    print("Você tem 15 anos ou mais. Portanto, sua compra não tem desconto. Você deve pagar R$ 90.")
    if dinheiro >= 90:
        print ("Parabéns pela compra!")
    else:
        print ("Valor insuficiente. Você precisa de R$ 90 para realizar a compra")
