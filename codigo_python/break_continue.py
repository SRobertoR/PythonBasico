def run():
    print("Sumas: ")
    for respuesta in "No":
        numero1 = int(input("Ingresa un numero: "))
        numero2 = int(input("Ingresa otro numero: "))
        suma = numero1 + numero2
        print("La suma de tus numeros es: " + str(suma))
        respuesta = input("Desea hacer otra suma: Si / No: ")
        respuesta = respuesta.capitalize()
        if respuesta == "Si":
            continue
        else:
            break


if __name__ == "__main__":
    run()