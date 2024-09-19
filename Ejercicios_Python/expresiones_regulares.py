"""Las expresiones regulares (llamadas RE, o regex, o patrones de regex) son esencialmente en un lenguaje de programación diminuto y altamente especializado incrustado dentro
de Python y disponible a través del módulo re. Usando este pequeño lenguaje, especificas las reglas para el conjunto de cadenas de caracteres posibles que deseas hacer
coincidir; este conjunto puede contener frases en inglés, o direcciones de correo electrónico, o comandos TeX, o cualquier cosa que desee"""
import re

cadena = 'Hola,21 esta es 32 una 10000cadena de 901 texto7'
pattern = r"\d+"
match = re.findall(pattern, cadena)
print(match)

email = 'c.monroy@ciencias.unam.mx'
pattern = r'\w+'
match = re.findall(pattern, email)
print(match)

if re.fullmatch(pattern, email):
    print('tu email es aceptable')