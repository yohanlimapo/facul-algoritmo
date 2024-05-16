# Menu Calculadora para converter criptomoeda em reais e vice-versa
# Funcionalidade: Conversão e Menu Interativo


while True:
    print("\n______________________________________________________")
    print("CONVERSÃO DE CRIPTOMOEDAS")
    print("______________________________________________________\n")
    print("1 -\tConverter Bitcoins em Reais.")
    print("2 -\tConverter Reais em Bitcoins.")
    print("3 -\tSair.\n")
    opcao = int(input("Escolha uma opção:\t"))
    valor_bitcoin = float(input("Quanto está o bitcoin em reais?\t"))
    if opcao == 1:
        bitcoin = float(input("Quantos bitcoins você tem?\t"))
        conversao_bit_reais = valor_bitcoin * bitcoin
        print("Resultado: R$",f'{conversao_bit_reais:.2f}')

    elif opcao == 2:
        reais = float(input("Quantos reais você tem?\t"))
        conversao_reais_bit = reais / valor_bitcoin
        print("Resultado: ", f'{conversao_reais_bit:.8f}', "Bitcoins.")

    elif opcao != 3: 
        print("Não entendi, digite um número válido.")

    else: 
        print("Tchau, até a próxima!")
        break