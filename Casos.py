#
# José Luis Zago Guevara  |  A01736278
# Actividad | Pruebas Sistema de Gestión de Cafetería
# TC3005B.502
#

import pytest
from ActividadCodigo import funcionBeb


casos = [
    
    #PRUEBAS QUE YA ESTABAN ESCRITAS EN CANVAS: 
    
    #El nombre del artículo es alfabético (válido)
    ("Té,8,12,16,20,24", "Válida"),
    #El nombre del artículo tiene menos de 2 caracteres de longitud (inválido)
    ("C,8,12,16", "Inválida: nombre de bebida debe ser entre 2 y 15 caracteres"),
    #El nombre del artículo tiene de 2 a 15 caracteres de longitud (válido)
    ("Cappuccino,10,12,14", "Válida"),
    #El valor del tamaño está en el rango de 1 a 48 (válido)
    ("Sprite,2,11,14,48", "Válida"),
    #El valor del tamaño es un número entero (válido)
    ("Coca Cola,2,12,16", "Válida"),
    #Los valores del tamaño se ingresan en orden ascendente (válido)
    ("Mocha,12,16,20,24,30", "Válida"),
    #Se ingresan de uno a cinco valores de tamaño (válido)
    ("Fanta,12", "Válida"),
    #El nombre del artículo es el primero en la entrada (válido)
    ("Delaware,12,16,20,24,36", "Válida"),
    #Una sola coma separa cada entrada en la lista (válido)
    ("Café,8,10,12,16", "Válida"),
    #La entrada contiene o no espacios en blanco (Inválida)
    ("Té Helado,,10,12,18,28", "Inválida: ingresa números enteros entre 1 y 48, sin espacios en blanco"),
    
    
    #PRUEBAS EXTRA:
    
    #Se ingresan más de 5 tamaños (inválido)
    ("Té Chai,10,20,31,32,30,44,50", "Inválida: ingresa de 1 a 5 números enteros separados por una coma"),
    #El nombre del artículo tiene más de 15 caracteres de longitud (inválido)
    ("Cappuccino Frappe,10,12,14", "Inválida: nombre de bebida debe ser entre 2 y 15 caracteres"),
    #Los valores del tamaño deben ir en orden ascendente (inválido)
    ("Chocomilk,41,15,16,9,31", "Inválida: los números del tamaño deben ir en orden ascendente"),
    #Se ingresa menos de 1 tamaño (inválido)
    ("Té Jengibre", "Inválida: ingresa de 1 a 5 números enteros separados por una coma"),
    #Se ingresa menos de 1 tamaño (inválido)
    ("9,Jugo Verde,41,23,3", "Inválida: el nombre de la bebida debe ir primero"),
    #El valor del tamaño es un negativo (inválido)
    ("Agua,12,3,42,-1", "Inválida: ingresa números enteros entre 1 y 48"),
    #Los valores del tamaño deben ir en orden ascendente (inválido)
    ("Té Ruda,27,21,20,9", "Inválida: los números del tamaño deben ir en orden ascendente"),
    #El valor del tamaño es menor que 1 (inválido)
    ("Coca,0,17,21,23", "Inválida: ingresa números enteros entre 1 y 48"),
    #El valor del tamaño es mayor que 48 (inválido)
    ("Chilate,2,10,17,50", "Inválida: ingresa números enteros entre 1 y 48"),
    #El nombre del artículo NO es alfabético (inválido)
    ("Agu@ Limón,9,11,19,21", "Inválida: nombre de bebida debe contener únicamente caracteres alfabéticos")
]




@pytest.mark.parametrize("entrada, expected", casos)
def test_funcionBeb(entrada, expected):
    assert funcionBeb(entrada) == expected