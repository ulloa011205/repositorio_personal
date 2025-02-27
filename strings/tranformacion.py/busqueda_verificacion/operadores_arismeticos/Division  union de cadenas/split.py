#split()
#Divide una cadena en una lista usando un separador.
frutas='hola mi nombre es lester'
frutas=frutas.split()
print(frutas)
#se agrega como para asi dividir mejor las plabras al momento de volverla lista
fruta="naranja,mango,sandia"
fruta=fruta.split(',')
print(fruta)
# se agrega ('',#)sirve para separar las palabras segundo el numero de ellas
colores='rojo azul amarillo rojo rosa'
colores=colores.split(' ', 2)
print(colores)