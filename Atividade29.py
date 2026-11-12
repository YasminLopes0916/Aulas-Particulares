alunos = ["Gabriel", "Yasmin", "Rafaela", "Sheyla", "Terso", "Antonio"]
numero = int(input("Digite um número do aluno: "))

while numero > 5 or numero < 0:
    numero = int(input("Não existe esse aluno, escolha um número entre 0 e 5: "))
print(f"O aluno de número {numero} é: {alunos[numero]}.")

"""Vamos inventar uma lista dos alunos da nossa turma, 
Então o usuário irá fornecer um número, 
E vamos encontrar esse aluno na lista usando esse número como um índice da lista."""
"""pra selecionar um item da lista é só colocar o nome da variável (do input) no []. Pra colocar o print fora do laço (while) é só colocar sem a indentação E depois do while
não precisa de if pra barrar a repetição, basta substituir a variável input anterior pela alterada (Não existe esse aluno, escolha um número entre 0 e 5)"""