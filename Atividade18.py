#Exercicio18
preco = float(input("Por favor, digite o preço atual do produto: R$ "))
venda = float(input("Agora, digite a venda média mensal do produto: "))
if venda < 500 or preco < 30:
    novo_preco = preco + (preco * 10 / 100)
elif (venda >= 500 and venda < 1200) and (preco >= 30 and preco < 80): #não específico, pois não filtra inconsistencia de resposta
    novo_preco = preco + (preco * 15 / 100)
elif venda >= 1200 and preco >= 80: #outro erro, o correto era and e não or.
    novo_preco = preco - (preco * 20 / 100)
else:
    novo_preco = preco
print(f"O novo preço do produto é: R$ {novo_preco:.2f}")

#manter and em condicoes com mais de dois parenteses: nesse contexto especifico onde só poderia ser uma e a outra condição.