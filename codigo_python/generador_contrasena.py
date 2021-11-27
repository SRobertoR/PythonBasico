import random

def generar_contrasena():
    mayusculas = ["A","B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    simbolos = ["!","#","$","/","(",")"]
    numeros = ["1","2","3","4","5","6","7","8","9","0"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    
    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == "__main__":
    run()