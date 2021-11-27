def run():
    #Listas en python
    print("_____________________________________________________")
    print("Lista 1")
    numeros = [1, 2, 3, 4, 5]
    print(numeros)
    print("Agregamos un hola al final")
    numeros.append("Hola")
    print(numeros)
    print("Eliminamos un hola del final")
    numeros.pop(5)
    print(numeros)
    print("____________________________________________________")
    print("Listas 2")
    numeros2 = [6, 7, 8, 9, 10]
    print(numeros2)
    print("Sumamos las dos listas")
    lista_final = numeros + numeros2
    print(lista_final)
    print("Multiplicamos la lista por 5")
    print(lista_final * 5)


    #Lo mismo con tuplas son estaticas son mas rapidas pero no se pueden modificar / son inmutables
    print("Lo mismo con tuplas")
    mi_tupla = (1, 2, 3, 4, 5)
    print(mi_tupla)
    for numero in mi_tupla:
        print(numero)


if __name__ == "__main__":
    run()