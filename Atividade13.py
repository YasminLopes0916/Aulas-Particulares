#Exercicio13
objeto = input("Olá! Sou o inspetor Raglan, estou investigando o assassinato de Roger Ackroyd. Qual desses objetos - só pode escolher um - foi encontrado na cena do crime: uma faca, veneno, arma de fogo ou objeto contundente? ").lower().strip()
distancia = float(input("Distância do objeto até o corpo (em metros): "))
digitais = input("O objeto tinha impressões digitais visíveis? (sim/não): ")
if objeto == "faca":
    if distancia < 2:
        print("Faca encontrada perto do corpo: provável arma do crime.")
        if digitais == "sim":
            print(">> Evidência prioritária!")
    else:
        print("Faca encontrada longe do corpo: improvável, mas não descartar.")
elif objeto == "veneno":
    if distancia < 2:
        print("Veneno encontrado perto do corpo: provável arma do crime.")
        if digitais == "sim":
            print(">> Evidência prioritária!")
    else:
        print("Veneno encontrado longe do corpo: improvável, mas não descartar.")
elif objeto == "arma de fogo":
    if distancia < 2:
        print("Arma de fogo encontrada perto do corpo: provável arma do crime.")
        if digitais == "sim":
            print(">> Evidência prioritária!")
    else:
        print("Arma de fogo encontrada longe do corpo: improvável, mas não descartar.")
elif objeto == "objeto contundente":
    if distancia < 2:
        print("Objeto contundente encontrado perto do corpo: provável arma do crime.")
        if digitais == "sim":
            print(">> Evidência prioritária!")
    else:
        print("Objeto contundente encontrado longe do corpo: improvável, mas não descartar.")
else:
    print("Tipo de objeto não reconhecido pela investigação.")
 