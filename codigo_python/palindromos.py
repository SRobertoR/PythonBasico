def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
 

#funcion principal se puede llamar run o main
def run():
    palabra = str(input("Escribe una palabra: "))
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es un palindromo")
    else:
        print("No es un palindromo")


if __name__ == "__main__":
    run()