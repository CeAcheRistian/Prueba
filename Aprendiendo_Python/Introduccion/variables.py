#Las varaibles son direcciones en memoria para almacenaremos diferentes valores
#Se representan mediante etiquetas o nombres
#Se puede modificar su valor en tiempo de ejecución
# <nombre> = <valor>
#Deben ser nombres claros y precisos
nombre = "Christian"
nombre = 'Jesús'
#Para las varaibles con más de un nombre se ocupa el snake_case, nomeclatura usada por Python
nombre_completo = "Christian Jesús Monroy Gutiérrez"
#Existen palabras que no pueden ser usadas como etiquetas de variables, estas de denominan palabras reservadas, como lo son:
"""
False 	class 	is 	return
None 	continue 	lambda 	try
True 	def 	nonlocal 	while
and 	del 	not 	with
as 	elif 	or 	yield
assert 	else 	pass 	
break 	except 	raise 	
"""

#Python permite que una variable almacene diferetnes tipos de datos

variable = 5
variable = 'hola'
variable = True

#Se pueden crear multiples varibles en una sola línea de código, su valor se establece dependiendo el orden
#Se recomienda no crear más de tres en una sola línea y tengan una relación.

nombre, apellido, edad = 'Christian', 'Monroy', 27
