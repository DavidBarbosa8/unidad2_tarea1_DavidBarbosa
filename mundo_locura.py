"""
Realizar el siguiente ejercicio con la instrucción if..else Para el ingreso a la montaña rusa, 
el parque mundo locura valida que la persona tenga una altura igual o superior a 1.20, para ayudar 
a esta validación usted debe construir un programa que solicite la altura y muestre un mensaje 
indicando si la persona puede ingresar o no a la atracción. 

"""

nombre = input("Ingrese el nombre de la persona:\n")
altura = float(input("Ingrese la altura de la persona: \n"))

if altura < 1.20:
  print (f"{nombre} no es apt@ para ingresar a la atraccion")
else:
  print (f"{nombre} es apt@ para ingresar a la atraccion")
  
  