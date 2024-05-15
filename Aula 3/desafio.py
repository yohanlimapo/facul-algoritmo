# Suponha que você é um programador de Python e precisa desenvolver um programa que recebe um caractere digitado pelo teclado utilizando a função input() e retorne, utilizando a função print(), esse caractere convertido em Decimal, Hexadecimal e Binário, conforme a figura a seguir:

# Digite uma letra: Z
# Letra digitada foi: Z
# Seu valor em decimal é: 90
# Seu valor em hexadecimal é: 0x5a
# Seu valor em binário é: 0b1011010

# Neste Desafio, escreva um código em Python para resolver esse problema. Dica: pesquise sobre os métodos ord(), bin() e hex() da linguagem Python para resolver a questão.

# letter = input("Digite uma letra: ").upper()
# ascii_code = ord(letter)
# hex_code = hex(ascii_code)

# print("Letra digitada foi: " + letter)
# print("Seu valor em decimal é: ", ord(letter))
# print("Seu valor em hexadecimal é: ", hex(ord(letter)))
# print("Seu valor em binário é: ", bin(ord(letter)))

# Dificuldades encontradas no exercício:
# Entender o objetivo de fazer o ord(), porque precisei dele para fazer o restante. Confesso que colei para precisar continuar.







texto = "Alterando o valor de sep"
print(texto)
print("Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4", sep=' -- ')
print()

texto = "Alterando o valor de sep e end"
print(texto)
print("Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4", sep=' -x- ', end="...\n")
print()

raio = 3
pi = 3.1415
area = pi*raio*raio
print("Raio do círculo:", raio, "cm")
print("Area do círculo:", raio, "cm²")
print("\nEita!\t\tViu?\n")

print("Dia\tMês\tAno\n30\tMaio\t1997\n08\tMaio\t2024")
print()

# name = input("Qual seu nome?\t")
# print()
# print("Fala,", name+"! Tranquilo?")
# print()

# name = input("Qual seu nome?\t\t\t")
# apelido = input("Como gostaria de ser chamado?\t")
# idade = int(input("Quantos anos você tem?\t\t"))
# altura = float(input("Qual a sua altura(m)?\t\t"))
# peso = float(input("Qual seu peso(kg)?\t\t"))

# print()
# print("Fala,",name,"de",str(idade),"anos!", "Tranquilo?")
# print("Mas é melhor te chamar de", apelido+", não é mesmo?")
# print("Com",str(peso)+"kg e tendo",str(altura)+"m... É bom continuar assim!")
# print()






# Conversão de temperatuas
# Comando input solicita o usuário a digitar uma temperatura
# Método float faz o casting da string para um valor numérico

# celsius = float(input("Digite a temperatura em Celsius:\t"))
# conversaoCelsiusFahrenheit = (celsius*9/5)+32   # Conversão para Fahrenheit
# # Resultado no console
# resultado = print("A temperatura de",str(celsius)+"ºC, em Fahrenheit é de:",str(conversaoCelsiusFahrenheit)+"ºF")







# Método format
# mensagem = "Valor decimal: {0}\nValor Hexadecimal: {1}"
# print("Programa para converter decimal para hexa")
# print()

# num_dec = int(input("Digite um número: "))
# print()

# num_hex = format(num_dec, "X")
# print()

# print(mensagem.format(num_dec,num_hex))









# Método format() formatando valores numéricos
# print("Programa para calcular real para dólar\n")

# real = float(input("Digite um valor em reais: R$"))
# print()

# dolar = float(input("Digite o valor do dólar atual: US$"))
# print()

# valor_convert = real/dolar
# print("R${0:.2f} valem U$ {1:.2f}".format(real,valor_convert))







# Método eval()
# equacao = input("Escreva uma equação: ")
# x = eval(input("Escreva um valor de x: "))

# print(equacao,"=",eval(equacao), "se x={0}".format(x))






# Método strftime
from datetime import datetime

hoje = datetime.now()
ano = hoje.strftime("%Y")
print("Ano:",ano)
mes = hoje.strftime("%m")
print("Mês:",mes)
dia = hoje.strftime("%d")
print("Dia:",dia)