#La librería Datetime incluye lo que dice su nombre, desde años,meses,dias,horas,minutos,segundos y milisegundos.
#Se puede convertir cadenas de texto en fechas, si se sigue el formato específico y el método y viceversa, aritmetica y comparación de fechas
"""Los tipos de datos a fondo:
date(año, mes, dia) : Devuelve un objeto de tipo date que representa la fecha con el año, mes y dia indicados.
time(hora, minutos, segundos, microsegundos) : Devuelve un objeto de tipo time que representa un tiempo la hora, minutos, segundos y microsegundos indicados.
datetime(año, mes, dia, hora, minutos, segundos, microsegundos) : Devuelve un objeto de tipo datetime que representa una fecha y hora con el año, mes, dia, hora, minutos, segundos y microsegundos indicados.
Para representar el tiempo transcurrido entre dos fechas se utiliza el tipo timedelta:
timedelta(dias, segundos, microsegundos) : Devuelve un objeto del tipo timedelta que representa un intervalo de tiempo con los dias, segundos y micorsegundos indicados."""

#Todos estos se deben importar, dependiendo de qué se necesite
from datetime import date, time, datetime, timedelta

fecha_actual = datetime.today() #también se puede .now() el cual puede dar la zona horaria aparte de la fecha y hora del momento que se ejecuta

fecha_nacimiento = datetime(1997, 7, 1, 2, 30, 17)

anios_transcurridos = fecha_actual.year - fecha_nacimiento.year
print(anios_transcurridos)

#El método strf dota de otro formato a la fecha
""""Para todos los formatos, consultar la documentación"""
otros_formatos = fecha_nacimiento.strftime('%W') #semanas transcurridas
otros_formatos = fecha_nacimiento.strftime('%w') #dia de la semana en número, el lunes es 1
otros_formatos = fecha_nacimiento.strftime('%p') #Especifica si es am o pm
otros_formatos = fecha_nacimiento.strftime('%A') #Nombre del día
otros_formatos = fecha_nacimiento.strftime('%Z') #Zona horaria
otros_formatos = fecha_nacimiento.strftime('%x') #Formato de la version local, mes/dia/año
otros_formatos = fecha_nacimiento.strftime('%X') #Formato de la version local para el tiempo
otros_formatos = fecha_nacimiento.strftime('%Y') #Año
otros_formatos = fecha_nacimiento.strftime('%B') #Nombre del mes
otros_formatos = fecha_nacimiento.strftime('%m') #Mes como numero
otros_formatos = fecha_nacimiento.strftime('%d') #Día del mes
otros_formatos = fecha_nacimiento.strftime('%f') #milisegundo
otros_formatos = fecha_nacimiento.strftime('%d/%m/%y') #para la fecha como se conoce normalmente
otros_formatos = fecha_nacimiento.strftime('%H:%M:%S') #para el tiempo en horas minutos y segundos
print(otros_formatos)
