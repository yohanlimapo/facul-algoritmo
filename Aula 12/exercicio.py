varA=3
varB=0
for num in range (varA):
    varB+=num**2
print(varB)
# 3 é o limite, então não haverá o cálculo de 3^2, apenas: 0; 1; 2

lista=["abacaxi","maça","uva","melão"]
for fruta in lista:
    qtdeLetras=0 #Necessário declarar a variável
    for letras in fruta:
        qtdeLetras+=1
    print(fruta,qtdeLetras )

dados=[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
for linha in dados:
    for coluna in linha:
        print(coluna)

for numerador in range(10):
    print("Tabuada do número",numerador)
    for multiplicador in range(10):
        print(numerador*multiplicador)

tabela=[]
contador=1
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(contador)
        contador+=1
    tabela.append(linha)
print(tabela)
