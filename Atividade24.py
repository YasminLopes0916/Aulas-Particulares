capricho = 10
ingredientes = 10
critico = "neutro"
while not(critico == "impressionado" or critico == "horrorizado"):
    opiniao_capricho = int(input("Escolha uma quantidade de pontos para gastar de capricho: "))
    opiniao_ingredientes = int(input("Escolha uma quantidade de pontos para gastar de ingredientes: "))

"""Começamos com 10 pontos de capricho e 10 de ingredientes
Você irá continuar trazendo pratos até o crítico ficar impressionado ou horrorizado.
Para cada prato, o usuário deve escolher uma quantidade de pontos para gastar de capricho e ingredientes."""
#As condições impressionado e horrorizado irão parar o laço de repetição.
#Pra inverter o que eu quero uso note: while not(critico == "impressionado" or critico == "horrorizado")
#Além da forma while not (usada nessa atv) poderia usar; while critico == "neutro"; 
#Ou ainda while critico != "impressionado" and cirtico != "horrorizado".