""""El formato json y xml son ficheros, así como un txt. Son ficheros que sirven para estructurar datos. Tienen especificaciones más profundas
JSON: JavaScript Object Notacion. JSON es un formato usado para almacenar o representar datos. Sus usos más frecuentes incluyen desarrollo web y creación de archivos de configuración.
Su estructura de datos es muy similar a un diccionario de Python. 'llave': <valor>
Se debe importar json para usar los objetos
Existen cambios en los tipos de datos entre Python y JavaScript, hay que considerarlos al trabajar con json."""
import json, os

archivo_json = 'presentacion.json'
presentacion = {
            'nombre': 'Christian',
            'edad': 27,
            'Fecha de Nacimiento': '01/07/1997',
            'Lenguaje': ['Python', 'JavaScript']
        }

def creacion_json():

    with open(archivo_json, 'w') as arc:
        #Con la funcion load() pasas de un json a un dict y con dumps() pasas de un dict a un json
        #Para escribir en un archivo json se usa la funcion dump(), el primer argumento es un objeto y el segundo es el archivo
        json.dump(presentacion,arc, indent=4) #El ident es para que sea más legible, solo es la identación
        #Para leer un json es loads()

creacion_json()
#leemos e imprimimos en consola, después se elimina el archivo
with open(archivo_json, 'r') as a:
    print(a.read())
os.remove(archivo_json)

"""Por otra parte, XML es un lenguaje de marcado muy utilizado en la web bastante versatil.
Ocupa "tags" que, como en html, se abren  y cierran, delimitando y albergando elementos.
Todo xml tiene un nodo raíz
Casi de ley debemos importar la libreria ElementTree para un mejor manejo del archivo."""
import xml.etree.ElementTree as ET #Por convencion es ET

archivo_xml = 'presentacion.xml'

def creacion_xml():
    #Creamos el nodo principal
    root = ET.Element("nodo_raiz")
    '''
    #Creamos los subnodos. Se especifica como argumento de quién es hijo y un nombre
    child = ET.SubElement(root,'nombre')
    #Ahora especificamos el texto del hijo
    child.text = 'Christian' '''
    #Reutilizaremos el diccionario con la informacion a introducir al xml
    for key,value in presentacion.items():
        #Recorremos el diccionario obteniendo sus llaves y valores e introduciendolos como hijos de la raiz principal con los datos que ya teníamos
        child = ET.SubElement(root, key)
        if isinstance(value, list): #Este metodo retorna un valor booleano, si el objeto pasado es del tipo de dato del segundo argumento
            for element in value:
                ET.SubElement(child, 'item').text = element
        else:
            child.text = str(value) #Nos aseguramos que sea puro texto lo que se introduzca en el texto

    #Se crea un arbold ejerarquias para ya crear el xml
    tree = ET.ElementTree(root)

    #Al ser un fichero, tiene una funcion write()
    tree.write("presentacion.xml")

creacion_xml()

#Para leer un xml
with open(archivo_xml, 'r') as a:
    print(a.read())

#Para borrar un xml
os.remove(archivo_xml)


creacion_json()
creacion_xml()
class Data():
    def __init__(self,name, age, date, languages) -> None:
        self.name = name
        self.age = age
        self.date = date
        self.languages = languages


with open(archivo_xml, 'r') as a:
    #Pasamos de un xml a una cadena 
    root = ET.fromstring(a.read())
    nombre = root.find('nombre').text
    edad = root.find('edad').text
    fecha_nacimiento = root.find('Fecha de Nacimiento').text
    lenguajes = root.find('Lenguaje').text

    user = Data(nombre,edad,fecha_nacimiento,lenguajes)
