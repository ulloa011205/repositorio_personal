#clasificacion de frases segun de la longitud
frase=str(input('escribir frase:'))
if len(frase)<=20:
    print('Es corta')
elif 20<=len(frase)<=50:
    print('Es media')
else :
    print('Es larga')
