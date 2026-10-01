frequencia = int(input("Em %, digite a frequência do aluno nas aulas (0 a 100): ")) 
media_final = float(input("Digite a média do nas disciplinas do semestre (0.0 a 10.0): "))
if (frequencia < 75) or (media_final < 7):
    print("Seu perfil não atende aos requisitos da bolsa. O valor será R$ 500!")
elif (frequencia >= 90) and  (media_final >= 9):
    print("Seu perfil supera os requisitos da bolsa. O valor será R$ 900!")
else:
    print("Seu perfil atende aos requisitos da bolsa. E o valor será de R$ 700!")





#lembrar de colocar casos especiais sempre no inicio do encadeamento (como idade < 12 e fraquencia/nota > 90/10)
"""Média do aluno nas disciplinas do semestre (número, pode ter casas decimais). Frequência do aluno nas aulas, em porcentagem (número, ex: 85 para 85%)
Lógica pedida:
Calcule o valor da bolsa com base em faixas que combinam média e/ou frequência, usando and/or dentro das condições (igual ao exercício de exemplo):
Se a média for baixa ou a frequência for baixa (defina os limites, ex: média abaixo de 7 ou frequência abaixo de 75%) → valor de bolsa reduzido (ex: aplicar um
desconto percentual sobre um valor base) media < 7 e frequencia < 75 (500)
Se média e/ou frequência estiverem numa faixa intermediária → valor de bolsa padrão media>=7 e frequencia>=75 (700)
Se média e/ou frequência estiverem numa faixa alta → valor de bolsa com bônus (acréscimo percentual) media>=9 e frequencia>=90 (900)
Caso nenhuma das condições anteriores se aplique → valor de bolsa base, sem alteração
Pense num valor base de bolsa (ex: R$ 700,00) definido no início do código, antes dos ifs, para servir de referência nos cálculos de desconto/bônus."""