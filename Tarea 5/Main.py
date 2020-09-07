import re
letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "1234567890"
diccionario = {(0,letras):2, (0,"_"):1 , (1,"_"):1 , (1,letras):3, (2,letras):2, (2,numeros):4,(3,letras):3 , (3,numeros):4}


def automata(cadena, actual, transision, aceptacion):
    if cadena == "":
        return actual in aceptacion
    else:
       
        caracter = cadena[0]

        if caracter in letras:
            caracter = letras
        elif caracter in numeros:
            caracter = numeros 

        if (actual,caracter) in transision:

            destino = transision[(actual,caracter)]
            nuevaCadena = cadena[1:]
            return automata(nuevaCadena,destino,transision,aceptacion)
        else:
            return False
        
print(automata("__servidor1",0,diccionario,[4]))
print(automata("3servidor",0,diccionario,[4]))