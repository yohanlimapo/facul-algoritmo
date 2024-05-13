op_validos = ['+', '-', '*','/']

while True:
    e = input("Digite o valor a esquerda do operador: ")
    if e.isdigit():
        op = input(f'digite o operador. Opções: {op_validos} ')
    else:
        print("Número inválido!")    
        continue
    d = input("Digite o valor a direita do operador: ")
    if d.isdigit():
        if op in op_validos:
            if op == '/' and d == '0':
                print("Divisão por zero! Tente novamente.")
                continue
            expressao = e + ' ' + op + ' ' + d
            print(e, op, d, "=", eval(expressao))
            break
        print("Valores ou operador incorreto!")
    else: 
        print("Número inválido!")

# ​​​​​​​​​​​​​​Com base nessas informações, responda:
# A) Qual função do Python poderia ser usada para verificar se o que foi digitado, para o valor que vai a esquerda ou a direita do operador, é um valor numérico?
# B) Como ficaria a expressão lógica que está sendo avaliada pela instrução if?

