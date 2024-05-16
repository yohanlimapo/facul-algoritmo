#sensação térmica
temperatura = float(input("Quantos graus ºC está fazendo?\t"))
if temperatura < 7: print("Congelando!")
elif temperatura <10: print("Frio!")
elif temperatura < 26: print("Ótimo!")
else: print ("Muito quente!")