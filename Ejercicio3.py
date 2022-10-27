"""
Escribe un programa que calcule el mínimo y el máximo de una
lista de números enteros positivos introducidos por el usuario. La lista
finalizará cuando se introduzca un número negativo

"""


def MaxYMin(a):
    '''
    Funcion Ejercicio 3 para mostrar el maximo y el minimo de una lista dada que acaba cuando se introduce el 0.
    Recibe: 
        - Una lista 'a' de longitud x que acaba cuando se introduce el 0
    Devuelve:
        - El maximo de la lista dada
        - El minimo de la lista dada 
    '''

    max = a[0]
    min = a[0]

    for i in a:
        if max < i:
            max = i
        if min > i:
            min = i
    return {'Maximo':max,'Minimo': min}



def main():
    #Ejercicio 3
    print('Testing Ejercicio 3: Maximo y Minimo de una lista dada que termina cuando se introduce el 0')
    print('\n')
    n = 1
    lista = []
    while n != 0:
        n = int(input('Introduce un numero '))
        lista.append(n)
    print(lista)
    print(MaxYMin(lista))
    print(end = '\n')



if __name__ == "__main__":
    main()