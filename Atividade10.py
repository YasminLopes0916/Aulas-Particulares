#Exercicio10
nome_convidado = input("Boa noite! Bem vindo(a) a Mansão Fernly Park. Qual o seu nome? ").strip().lower()
#Extinguindo possibilidade de burlar o sistema com espaços entre nome e sobrenome ou entre letras no caso dos barrados no baile
nome_convidado = nome_convidado.replace("_" , " ")
nome_convidado = " ".join(nome_convidado.split())
idade_convidado = int(input("Qual a sua idade? "))
#Barrados no Baile
lista_convidados_proibidos = ["caroline sheppard", "bart", "draco malfoy"]
if nome_convidado in lista_convidados_proibidos:
    print("Você não pode entrar!!!")
elif idade_convidado < 12:
    print("Não pode entrar, é hora de dormir.")
elif idade_convidado < 18:
     print("Pode entrar, mas só até as 22h.")
else:
    print("Pode entrar à vontade!")
###Ainda há muitos erros de "vulnerabilidade" no código, como por exemplo, ao inverter o nome com sobrenome ("Sheppard Caroline") ou o nome todo ("traB")
###Dúvida, eu poderia colocar o else, como na atividade 8, que quando o user digita besteira ele recusa no ato?

