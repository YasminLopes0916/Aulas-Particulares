capricho = 10
ingredientes = 10
critico = "neutro"
while critico == "neutro":
    opiniao_capricho = int(input("Escolha uma quantidade de pontos para gastar de capricho: "))
    opiniao_ingredientes = int(input("Escolha uma quantidade de pontos para gastar de ingredientes: "))
    if opiniao_capricho > capricho:
        print(f"Você escolheu {opiniao_capricho}, mas só tem {capricho}")
        opiniao_capricho = capricho  # substitui pelo valor que você realmente tem
        capricho = 0
    elif opiniao_capricho < 0:
        print(f"Você escolheu {opiniao_capricho}, então você vai usar 0.")
        opiniao_capricho = 0  # substitui o valor negativo por 0
    else:
        capricho -= opiniao_capricho
    if opiniao_ingredientes > ingredientes:
        print(f"Você escolheu {opiniao_ingredientes}, mas só tem {ingredientes}")
        opiniao_ingredientes = ingredientes
        ingredientes = 0
    elif opiniao_ingredientes < 0:
        print(f"Você escolheu {opiniao_ingredientes}, então você vai usar 0.")
        opiniao_ingredientes = 0
    else:
        ingredientes -= opiniao_ingredientes

    nivel = 1.5 * opiniao_capricho + opiniao_ingredientes - 3
    print(f"O nível do seu prato é {nivel}")

    if nivel == 10:
        critico = "impressionado"
        print("O crítico ficou impressionado! Você ganhou a estrela Michelin! ⭐")
    elif 8 <= nivel <= 12:
        print("O crítico continua neutro. Você pode fazer outro prato.")
        print(f"Pontos restantes -> capricho: {capricho}, ingredientes: {ingredientes}")
    else:
        critico = "horrorizado"
        print("O crítico ficou horrorizado e foi embora.")


"""Nesse atividade a lógica era usar a substituição em vez de atualização (somar/subtrair). O nível do prato é 1.5* capricho + ingredientes-3. Se o nível for exatamente 10, o crítico fica  impressionado e te dá a 
estrela Michelin. Se o nível for entre 8 e 12, o crítico continua neutro e você pode fazer outro prato para tentar de novo.
Caso contrário, ele fica horrorizado e vai embora."""

#Na atv o capricho maior que o ingrediente já pode conferir a estrela Michelin
"""O armazenamento e na lista o primeiro colocado é zero pois pra armazenar o zero tmb é usado e não deve ser desperdiçado. Por isso
a lista sempre começa no índice zero"""