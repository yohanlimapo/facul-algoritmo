# variavelArmazenaLeitura=LEITURASENSOR(sensor):
# TEMP_INIT: temperatura em graus C
# TEMP_EXT: temperatura em graus C
# UMIDADE: sensor de umidade do ar
# BOTAO: estado do BOTAO de PRONTO: retorna ON quando acionado e OFF caso contrário

# Acionamento:
# EXAUSTOR(estado):
# ON, liga exaustor
# OFF, desliga exaustor

# AQUECIMENTO(temperatura)
# Valor inteiro fixo
# OFF, desliga sistema de aquecimento

# TIMER(estado)
# SET, ativa o contador de tempo
# RESET, zera e desativa o contador de tempo
# TIME, retorna o tempo em minutos desde o acionamento


# Medir UMIDADE do ar interna e TEMPERATURA externa do forno
import time
UMIDADE = int(input("Qual a umidade do ar na parte interna do forno?\t"))
TEMP_EXT = int(input("Qual a temperatura da parte EXTERNA do forno?\t"))
TEMP_INT = int(input("Qual a temperatura INTERNA do fogo?\t"))

clima = input("Estamos no inverno? (S/N)\t")
if clima == "S" or "s":
    print("Iniciando desumidificação...")
    time.sleep(3)
    # Procedimento de DESUMIDIFICAÇÃO
    print("Início da desumidificação.")
    time.sleep(3)
    # Condicional para TEMPERATURA
    if TEMP_INT > 100: print ("Forno superaquecido, desligue agora!!!")
    elif TEMP_INT > 15 and UMIDADE <= 40:
        print("Acionar exaustor")
        EXAUSTOR = True
        time.sleep(2)
        print ("Exaustor ligado")
        time.sleep(5)
        
        UMIDADE = 5
        EXAUSTOR = False
        print("Desumidificação concluída.")
    else:
        print("Acionar aquecimento do forno e exaustor do ar.") #TEMP_INT < 15 and UMIDADE >= 40
        AQUECIMENTO = int(input("Qual a temperatura desejada?\t"))
        time.sleep(1)
        print("Desumidificação iniciada.")
        time.sleep(15)
        print("Desumidificação concluída.")

# Sem inverno, sem desumidificação
else: print("Pronto para a cocção")
time.sleep(3)
# Procedimento de COCÇÃO
print("Iniciando cocção...")
time.sleep(3)
if UMIDADE > 15:
    print("Acionar exaustor.")
    time.sleep(5)

    if TEMP_INT < 200:
        print("Acionar aquecimento para a temperatura de 380ºC")
        time.sleep(5)
        AQUECIMENTO = 380
        print("Temperatura atual: 380ºC")
        time.sleep(1)
    UMIDADE = 5
    print("Exaustor desligado.")
    time.sleep(2)

BOTAO = input("Inserir conteúdo para cocção - quando concluir digitar S").upper()
if BOTAO == "S":
    print("Aquecendo, volte em 3 horas.")
    time.sleep(20)
print("Cocção concluída.\nAquecimento desligado.")


