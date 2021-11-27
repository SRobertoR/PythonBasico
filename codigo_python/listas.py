numeros = [1,3,6]
print(numeros)
objetos = ["Roberto", "Olivares Rivera", "Estudiante"]
print(objetos)
print(objetos[0])
#Agregar datos a la lista
objetos.append(23)
print(objetos)
#Borrar datos de la lista  pop(indice que se desea borrar)
objetos.pop(1)
print(objetos)

#Recorrer la lista con un arreglo
for elementos in objetos:
    print(elementos)

#Slices invertir lista
print(objetos[::-1])