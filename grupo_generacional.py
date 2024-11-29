"""
Realizar el siguiente ejercicio con la instrucción if..elif..else Construir un programa que permita calcular el grupo generacional al cual pertenece una persona, para esto debe solicitar la edad y dependiendo del rango de edades mostrar a que grupo pertenece así:

Edades Grupo Generacional Menor o igual a 12 años Niño De 13 a 17 Adolescente De 18 a 34 Joven De 35 a 63 Adulto Mas de 63  Adulto mayor 

"""
edad = int(input("Ingresa por favor tu edad en numero entero \n"))

if edad <= 12:
  print ("Eres niño")
elif edad > 12 and edad <=17:
  print ("Eres adolescente")
elif edad > 17 and edad <= 34:
  print ("Eres Joven")
elif edad > 34 and edad <= 63:
  print ("Eres adulto")
else:
  print ("Eres adulto mayor")