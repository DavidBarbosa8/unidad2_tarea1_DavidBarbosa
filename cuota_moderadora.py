"""
Realizar el siguiente ejercicio con la instrucción if..else mediante condicionales anidados (es decir dentro de la instrucción else colocar una nueva condición if..else) La EPS “Mi Salud” ha solicitado su ayuda para la creación de un programa que permita calcular el valor de la cuota moderadora de un afiliado acorde a sus ingresos. Para esto, usted debe solicitar que digiten el ingreso del afiliado y mostrar la cuota moderadora acorde a esta tabla: Tabla 2 Rango de ingresos y su cuota moderadora. 
Rango de ingresos Valor de la cuota moderadora Menor a 2 salarios mínimos Entre 2 y 5 salarios mínimos 4000 15000 Mayor a 5 salarios mínimos 40000
"""

salario = float (input("Ingrese su salario mensual sin puntos ni comas \n"))
salario_minimo = 1300000

if salario < (salario_minimo * 2):
  print ("El valor de la cuota moderadora es $4.000")
else:
  if salario >= (salario_minimo * 2) and salario <= (salario_minimo*4):
    print ("El valor de la cuota moderadora es $15.000")
  elif salario < (salario_minimo * 5):
    print ("El valor de la cuota moderadora es $ 40.000")