#censurador de palabrascle
palabras=str(input('Escribir palabra '))
censurar=str(input('Escribir palabra a censurar '))
cambio=palabras.replace(censurar,'**')
print(cambio)