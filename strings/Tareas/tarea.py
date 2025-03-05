#verficacion de polindromos
Palabra=str(input('escribe una palabra '))
invertir=Palabra.lower()
invertir=invertir[::-1]
if invertir==Palabra.lower():
    print('Es polindromo')
else:
    print('No es polindromo]')