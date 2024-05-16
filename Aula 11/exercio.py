cont = 0
while True:
    cont +=1
    if(cont%2==0):
        continue
    if(cont>9):
        break
    print(cont,end=';')