numero = 0
while numero != 8:
    numero = int(input("Tente advinhar um número entre 1 e 10: "))
    if numero < 8:
        print(f"Tente um número maior que {numero}.")
    elif numero == 8:
        print(f"Parabéns! Você acertou o número secreto que é o: {numero}!")
    elif numero > 8:
        print(f"Tente um número menor que {numero}.")

#Cuidado com a indentação do while, a estrutura aninhada deve ficar dentro do while.
#se eu quero que uma pergunta se repita até o user acertar, tem que colocar dentro do while/loop
#inicializar a variavel antes do while! numero = 0 vem antes do while e da estrutura aninhadada
#Além disso é ela que vai botar uma trava na repetição pra ela não ficar infinita. Por isso precisa colocar um ou mais
#variáveis antes do while.
#numero = 0 isso porque não pode pode "chamar" a var no while sem antes regristrá-la.
#Quando ele for falso ele para de repetir.