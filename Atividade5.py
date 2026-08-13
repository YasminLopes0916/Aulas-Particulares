#Exercicio3
idade = int(input("Informe a sua idade? "))
dinheiro = input("Informe quantos reais você tem: ")
correcao_virgula = dinheiro.replace("," , ".")
dinheiro = float(correcao_virgula)
escolha = input("Escolha o produto (boneco, plug anal ou CNH): ")
escolha = escolha.lower()
if escolha == "boneco":
    if idade < 12:
        print("Você ainda é criança. Nesse caso, sua compra terá um desconto!")
        if dinheiro >= 10:
            print("Parabéns pela compra!")
        else: 
            print("Valor insuficiente. Você precisa de R$ 10 para realizar a compra.")
else:
    if escolha == "plug anal":
        if idade > 17:
            print("Você tem mais de 17 anos. Portanto, o produto não é restrito.")
            if dinheiro >= 100:
                print("Parabéns pela compra do seu lindo plug!!!")
            else:
                print("Você não tem dinheiro suficiente para comprar o plug anal!")
        else:
            print("Você tem menos de 18 anos. Portanto, o produto é restrito.")
    else:
        if escolha == "cnh":
            if idade < 12:
                print("Você ainda é criança! Nem com propina você consegue a CNH.")
            if 12 < idade < 18:
                print("Você é um adolescente. Nesse caso, você não tem nenhum desconto!")
                if dinheiro >= 2000:
                    print("Com esse valor você pagar a propina e obter sua CNH!")
                else: 
                    print("Valor insuficiente! Com esse valor irrisório você não consegue comprar nada.")
            if idade >= 18:
                print("Você é adulto! Nesse caso, a propina é só R$ 1000")
                if dinheiro >=1000:
                    print("Parabéns pela compra da CNH!")
                else:
                    print("Volte quando tiver o dinheiro da propina, seu pobre!")
        else:
            print("Opção inválida!")

















