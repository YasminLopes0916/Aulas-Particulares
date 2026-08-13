nota1 = float(input("Qual foi a sua nota na 1° avaliação? "))
nota2 = float(input("Qual foi a sua nota na 2° avaliação? "))
nota3 = float(input("Qual foi a sua nota na 3° avaliação? "))
media = (nota1 + nota2 + nota3)/3
if media < 5:
    print("Você foi reprovado.")
elif media < 10:
    print("Você foi aprovada!")
else:
    print("Parabéns! Você aprovou com nota máxima!")