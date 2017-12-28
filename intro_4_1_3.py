import numpy as np 
archivo=open('intro_4_1_3_height.txt','r')
leer_fila= archivo.readlines()
archivo.close()
height= []
for lista in leer_fila:
    # revisamos si tiene un salto de linea al final para quitarlselo.
    if lista[-1]=="\n":
        dato=lista[:-1].split(", ")
    else:
        dato=lista.split(", ")
    height.append(int(dato[0]))

archivo=open('intro_4_1_3_weight.txt','r')
leer_fila2= archivo.readlines()
archivo.close()
weight= []
for lista in leer_fila2:
    # revisamos si tiene un salto de linea al final para quitarlselo.
    if lista[-1]=="\n":
        dato=lista[:-1].split(", ")
    else:
        dato=lista.split(", ")
    weight.append(int(dato[0]))
