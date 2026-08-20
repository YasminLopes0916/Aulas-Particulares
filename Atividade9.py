nota1 = float(input("Qual a sua primeira nota? "))
if nota1 < 0 or nota1 > 10:
    print("Opção inválida! Como você colocou um valor inválido, vou interpretar como nota zero")
    nota1=0
nota2 = float(input("Qual a sua segunda nota? "))
if nota2 < 0 or nota2 > 10:
    print("Opção inválida! Como você colocou um valor inválido, vou interpretar como nota zero")
    nota2=0
nota3 = float(input("Qual a sua terceira nota? "))
if nota3 < 0 or nota3 > 10:
    print("Opção inválida! Como você colocou um valor inválido, vou interpretar como nota zero")
    nota3=0
media = (nota1 + nota2 + nota3)/3
if media == 10:
    print("Parabéns pelo A! Você teve a nota perfeita! ")
elif media >= 9:
    print("Parabéns pelo A! Você foi aprovado!")
elif media >=8:
    print("Parabéns pelo B! Você foi aprovado!")
elif media >=7:
    print("Parabéns pelo C! Você foi aprovado!")
elif media >=6:
    print("Parabéns pelo D! Você foi aprovado!")
elif media >=5:
    print("Parabéns pelo F! Você foi aprovado!")
else:
    print("Não foi dessa vez! Você tirou um F e foi reprovado! Tente novamente no próximo semestre!")


