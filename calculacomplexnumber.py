#valentina alvarado
#cnyt
#calculadora con numeros complejos

import math
from math import sqrt
def sumar(tpl1,tpl2):
    """ Esta función le ayuda a calcular la suma entre dos numeros complejos
        (tuple,tuple) ---> tuple"""
    sumareal = tpl1[0] + tpl2[0]
    sumaimg = tpl1[1] + tpl2[1]
    return (sumareal,sumaimg)
#
def multiplicar(tpl1,tpl2):
    """Esta función le ayuda a calcular la multiplicación entre dos numeros complejos
       (tuple,tuple)---> tuple"""
    real1 = tpl1[0] * tpl2[0]
    imag1 = tpl1[0] * tpl2[1]
    imag2 = tpl1[1] * tpl2[0]
    real2 = (tpl1[1] * tpl2[1]) * (-1)
    partereal = real1 + real2
    parteimag = imag1 + imag2
    return (partereal,parteimag)
#
def resta(tpl1,tpl2):
    """ Esta funcion le ayuda a calcular la resta entre dos numeros complejos
        (tuple,tuple) ---> tuple"""
    restareal = tpl1[0] - tpl2[0]
    restaimg = tpl1[1] - tpl2[1]
    return (restareal,restaimg)
#
def dividir(tpl1,tpl2):
    """Esta funcion le ayuda a calcular la division entre dos numeros complejos
        (tuple,tuple)--->tuple"""
    denominador = (tpl2[0] * tpl2[0]) + (tpl2[1] * tpl2[1] )
    numer1 = (tpl1[0] * tpl2[0]) + (tpl1[1] * tpl2[1])
    numer2 = (tpl2[0] * tpl1[1]) - (tpl2[1] * tpl1[0])
    real1 = round(numer1 / denominador,3)
    imaginario = round(numer2 / denominador,3)
    return (real1,imaginario)
#
def modulo(tpl1):
    """Esta funcion le ayuda a acalcular el modulo de un numero complejo
        (tuple) --> float"""
    modulo = (((tpl1[0])**2) + ((tpl1[1])**2))**(1/2)
    return round(modulo,2)
#
def conjugado(tpl1):
    """ esta funcion le ayuda a calcular el conjugado de un numero complejo
        (tuple)--->tuple"""
    conjugado1 = tpl1[1] * -1
    return (tpl1[0],conjugado1)
#
def polaracartesiana(tpl):
    """ esta funcion le ayuda a pasar de coordenadas polares a coordenadas cartesianas
        (tuple) --> tupla"""
    angulo = math.radians(tpl[1])
    a = round(tpl[0] * math.cos(angulo),3)
    b = round(tpl[0] * math.sin(angulo),3)
    return (a,b)
#
def fase(tpl):
    """ esta funcion le ayuda a caluclar la fase un numero complejo
        (tuple) --> float"""
    return(round(math.atan(tpl[1]/tpl[0]),2))




