"""
Escribir un programa que defina variables que representen el
número de días de un año, el número de horas que tiene un día, el número de
minutos que tiene una hora y el número de segundos que tiene un minuto. A
continuación, calcular el número de segundos que tiene un año y almacenar
el valor del cálculo en otra variable
"""


def SecEnAños(n):
    '''
    Funcion Ejercicio 1 para calcular numero de segundos en un año que recibe:
        - Un entero n
    Y devuelve: 
        - Un return de enteros
    '''
    dias = 365
    horas = 24
    minutos = 60
    segundos = 60

    return n * dias * horas * minutos * segundos



def main():
      #Ejercicio 1
    print('Testing Ejercicio 1: Cuantos segundos en N años?')
    print('\n')
    try:
        n = float(input("Numero de años? "))
        resultado1 = SecEnAños(n)
        print(n,' años tiene: ',resultado1, ' segundos')
        print(end = '\n')
    except TypeError:
        print('Error. Has introducido algo diferente a un numero. ')


if __name__ == "__main__":
    main()
