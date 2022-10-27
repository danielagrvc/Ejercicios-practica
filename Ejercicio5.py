"""
Escribe un programa que muestre por pantalla la lista de los 100
primeros números primos. Utilizar funciones para saber si un número es
primo. 
"""

def NumPrim(maximo):
    '''
    Funcion ejercicio 5 para mostrar los numeros primos en un intervalo.
    Recibe:
        - Un maximo el cual sirve comno limite superior del intervalo
    Devuelve:
        - Una lista con todos los nueros primos en ese intervalo
    '''
    respuesta = [x for x in range(2,maximo) if not [i for i in range(2, x-1) if not x%i]]
    return respuesta



def main():
    
    #Ejercicio 5
    print('Testing ejercicio 5: Mostrar los numeros primos en los 100 primeros numeros')
    print('\n')
    print(NumPrim(100))
    print(end = '\n')



if __name__ == "__main__":
    main()