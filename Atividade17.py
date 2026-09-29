#Exercicio17
tipo_de_avistamento = input("Qual equipamento avistou o veículo: câmera de trânsito, testemunha ocular, rastreador GPS ou posto policial? ")
velocidade = float(input("Qual era a velocidade do veículo no momento do avistamento. Informe a velocidade em km/h: "))
placa_veiculo = input("Responda com sim ou não: A placa do veículo foi identificada? ")
limite_velocidade = 100:

if tipo_de_avistamento == "câmera de trânsito":
    print("Entendi. O equipamento que avistou foi a câmera de trânsito.")
    if velocidade > limite_velocidade:
        print("Veículo em fuga ativa, alta prioridade.")
        if placa_veiculo == "sim":
            print("Acionar bloqueio policial imediato.")
        else:
            print("Enviar unidades para rastrear visualmente.")
    else:
        print("Pode ser apenas trânsito comum, prioridade baixa.")
elif tipo_de_avistamento == "testemunha ocular":
    print("Entendi. Quem avistou foi uma testemunha ocular.")
    if velocidade > limite_velocidade:
        print("Veículo em fuga ativa, alta prioridade.")
        if placa_veiculo == "sim":
            print("Acionar bloqueio policial imediato.")
        else:
            print("Enviar unidades para rastrear visualmente.")
    else:
        print("Pode ser apenas trânsito comum, prioridade baixa.") 
elif tipo_de_avistamento == "rastreador GPS":
    print("Entendi. O equipamento que avistou foi o rastreador GPS.")
    if velocidade > limite_velocidade:
        print("Veículo em fuga ativa, alta prioridade.")
        if placa_veiculo == "sim":
            print("Acionar bloqueio policial imediato.")
        else:
            print("Enviar unidades para rastrear visualmente.")
    else:
        print("Pode ser apenas trânsito comum, prioridade baixa.") 
elif tipo_de_avistamento == "posto policial":
    print("Entendi. O equipamento que avistou foi o posto policial.")
    if velocidade > limite_velocidade:
        print("Veículo em fuga ativa, alta prioridade.")
        if placa_veiculo == "sim":
            print("Acionar bloqueio policial imediato.")
        else:
            print("Enviar unidades para rastrear visualmente.")
    else:
        print("Pode ser apenas trânsito comum, prioridade baixa.")
else:
    print("Tipo de avistamento não reconhecido.")