# Suponha que você é um programador de Python e precisa desenvolver um programa que recebe um caractere digitado pelo teclado utilizando a função input() e retorne, utilizando a função print(), esse caractere convertido em Decimal, Hexadecimal e Binário, conforme a figura a seguir:

# Digite uma letra: Z
# Letra digitada foi: Z
# Seu valor em decimal é: 90
# Seu valor em hexadecimal é: 0x5a
# Seu valor em binário é: 0b1011010

# Neste Desafio, escreva um código em Python para resolver esse problema. Dica: pesquise sobre os métodos ord(), bin() e hex() da linguagem Python para resolver a questão.

letter = input("Digite uma letra: ").upper()
ascii_code = ord(letter)
hex_code = hex(ascii_code)

print("Letra digitada foi: " + letter)
print("Seu valor em decimal é: ", ord(letter))
print("Seu valor em hexadecimal é: ", hex(ord(letter)))
print("Seu valor em binário é: ", bin(ord(letter)))

# Dificuldades encontradas no exercício:
# Entender o objetivo de fazer o ord(), porque precisei dele para fazer o restante. Confesso que colei para precisar continuar.