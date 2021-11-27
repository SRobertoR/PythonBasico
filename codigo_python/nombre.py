nombre = str(input("¿Cual es tu nombre?: "))
#El punto upper() nos ayuda a poner el texto en mayusculas 
print(nombre.upper())

#Colocar la primera letra mayuscula si son dos palabras solo modifica la primera 
print(nombre.capitalize())

#Limpia espacios al principio y al final 
print(nombre.strip())

#Cambia toda la cadena a minusculas
print(nombre.lower())

#cambia letras en este caso cambia todas las o y las sustituye con a
print(nombre.replace("o","a"))
#indices
print(nombre[0])
#Cuantoscaracteres tiene la cadena // es una funcion dell int
print(len(nombre))
print(len("Hola a todos estoy aprendiendo"))

#slices o bloques
nombre1 = str(input("¿Ingresa una cadena y la parto?")) 
nombre1 = nombre1.strip()
primera = nombre1[0:3]
segunda = nombre1[4:]
print("Las primeras 3 letras son:   " + primera + "   y el resto es: " + segunda)
#Cantidad de pasos para llegar a donde quieres corta cada dos letras en el ejemplo de abajo comenzando en la posicion 1 a 4
print(nombre1[1:4:2])
# Del uno hasta el final en pasos de 3 en 3
print(nombre1[1::3])
#Desde el final al inicio seria asi 
print(nombre1[::-1])