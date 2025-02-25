#str.zfill(12)
#rellena con ceros hasta llenar el tamaño de la cadena
cadena=int(input('ingresa un numero '))
cadena=str(cadena).zfill(3)
print(f'tu  numero es:{cadena}')
#zfill solo trabaja con tipos de variables str por ende hay que onverti el int en str