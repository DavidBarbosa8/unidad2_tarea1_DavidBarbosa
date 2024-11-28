"""
Realizar el siguiente ejercicio con la instrucción if..else El profesor Juan ha solicitado su ayuda 
para calcular el promedio de 5 notas del curso de 1 estudiante. Usted debe construir un programa que 
solicite las 5 notas, las sume y muestre el promedio, además si el promedio es mayor o igual a 3 debe 
decir curso aprobado, sino entonces curso no aprobado 

"""
estudiante = input("Ingrese el nombre del estudiante: \n")
n1 = float(input("Ingrese la nota 1 por favor:\n "))
n2 = float(input("Ingrese la nota 2 por favor: \n"))
n3 = float(input("Ingrese la nota 3 por favor: \n"))
n4 = float(input("Ingrese la nota 4 por favor: \n"))
n5 = float(input("Ingrese la nota 5 por favor: \n"))

promedio = (n1+n2+n3+n4+n5)/5
print (f"El promedio del estudiante {estudiante} es: {promedio}")

if promedio >= 3.0:
    print ("Curso aprobado")
else:
    print ("Curso no aprobado")