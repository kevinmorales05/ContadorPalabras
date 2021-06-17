# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 17:21:28 2021

@author: kevde
"""

#Trabajo en Clase
#Contar cantidad de ocurrencia de las palabras: harry, potter, child

def leerLibro():
    file = open('harrypotter.txt', encoding='utf8')    
    linea = file.readline()
    while linea!="":
        #print(linea)
        linea = file.readline()
        frase=" Avanzando frontend de la Web: Home y Login para conectar la Api al crud de usuarios"
    analizarLibro(frase)
    file.close()
    
    
def analizarLibro(texto):
    texto.lower()
    print(texto)
    palabra = input('Que palabra desea contabilizar?')
    if palabra != "":
        print('Iniciando Contabilidad de palabra ...')
        cantidad = texto.count('harry')
        print('La cantidad de veces que se repite ' + palabra + ' es ' + str(cantidad))
    
leerLibro()
texto = 'la vida es vida porque es para vivirla y la vida se acaba'
print(texto.count('vida'))