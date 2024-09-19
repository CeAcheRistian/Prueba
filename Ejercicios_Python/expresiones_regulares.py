"""Las expresiones regulares (llamadas RE, o regex, o patrones de regex) son esencialmente en un lenguaje de programación diminuto y altamente especializado incrustado dentro
de Python y disponible a través del módulo re. Usando este pequeño lenguaje, especificas las reglas para el conjunto de cadenas de caracteres posibles que deseas hacer
coincidir; este conjunto puede contener frases en inglés, o direcciones de correo electrónico, o comandos TeX, o cualquier cosa que desee"""
import re

#https://cheatography.com/davechild/cheat-sheets/regular-expressions/
#https://docs.python.org/es/3/library/re.html#module-re

#Expresión regular para encontrar números en una cadena
cadena = 'Hola,21 esta es 32 una 10000cadena de 901 texto7'
pattern = r"\d+"
match = re.findall(pattern, cadena)
print(match)

#Expresión regular para validar email
email = 'c.monroy.gtz@gmail.com'
pattern = r'^([\w._]+@\w+\.[a-z]{2,3})$'
match = re.search(pattern, email)
print(match)

#Expresión regular para validar url
url = "https://www.google.com"
pattern = r'^(https?://(www\.)?|www\.)(\w+)\.?(\w+)*\.[a-z]{2,3}$'
match = re.search(pattern, url)
print(match)

#Expresión regular para validar número de teléfono
telefono = '55-43-22-99-52'
pattern = r'^(\d{2}\D?){5}$'
match = re.search(pattern, telefono)
print(match)