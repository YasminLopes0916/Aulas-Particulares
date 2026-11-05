capricho = 10
ingredientes = 10
critico = "neutro"
while critico == "neutro":
    opiniao_capricho = int(input("Escolha uma quantidade de pontos para gastar de capricho: "))
    opiniao_ingredientes = int(input("Escolha uma quantidade de pontos para gastar de ingredientes: "))
    if opiniao_capricho > capricho: #condição (if) dentro do while
        print (f"Você escolheu {opiniao_capricho}, mas só tem {capricho}")
    if opiniao_ingredientes > ingredientes:
        print (f"Você escolheu {opiniao_ingredientes}, mas só tem {ingredientes}") 

"""Continua: Se o usuário escolher uma quantidade maior de pontos do que tem, ele irá usar tudo que tem ao invés do número escolhido. 
Se o usuário tentar usar uma quantidade negativa, usa 0. 
Em casos normais, subtraia a quantidade de pontos que ele escolheu usar do total de pontos que ele tem disponível.
O nível do prato é 1.5* capricho + ingredientes-3"""