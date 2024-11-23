"""	
Una persona ha sido asesinada en la noche de Halloween 🔪. Usando un hechizo 🧙‍♀️, hemos conseguido escuchar su último susurro pero es muy debíl y no nos permite identificar quién pudo ser el asesino.

La información que nos proporciona:

whisper: cadena de texto que representa lo que la víctima intentó decir antes de morir

suspects: lista de cadenas que representa los nombres de todos los sospechosos.

Hay que tener que el susurro whisper tiene algunas reglas:

    Cada ~ representa una letra incierta en el susurro.
    Cada posición del susurro es una posición del nombre del asesino.
    La longitud del whisper no siempre representa la longitud completa del nombre, ya que la víctima pudo haber muerto antes de terminar de decirlo.
    Pero si el último carácter del susurro es una $, entonces el nombre del asesino terminaba ahí.

¡Tu objetivo es descubrir quién pudo ser el asesino! Debes devolver:

    Si solo un nombre encaja con el patrón del susurro, retorna ese nombre.
    Si hay varios nombres que encajan, retorna todos los nombres separados por comas.
    Si ningún nombre encaja, retorna una cadena vacía ("").

Las mayúsculas y minúsculas de las letras no importan.

const whisper = 'd~~~~~a';
const suspects = ['Dracula', 'Freddy Krueger', 'Jason Voorhees', 'Michael Myers'];

findTheKiller(whisper, suspects); // -> 'Dracula'

const whisper2 = '~r~dd~';
const suspects2 = ['Freddy', 'Freddier', 'Fredderic']

findTheKiller(whisper2, suspects2); // -> 'Freddy,Freddier,Fredderic'

const whisper3 = '~r~dd$';
const suspects3 = ['Freddy', 'Freddier', 'Fredderic']

findTheKiller(whisper3, suspects3); // -> ''

const whisper4 = 'mi~~def';
const suspects4 = ['Midudev', 'Midu', 'Madeval']

findTheKiller(whisper4, suspects4); // -> ''

"""

import re

def find_the_killer(whisper:str , suspects:list) -> str:
    coincidences = []

    whisper = whisper.replace('~','\w*')

    for suspect in suspects:
        pattern = r'{}'.format(whisper)

        match = re.search(pattern, suspect, re.IGNORECASE)

        if match != None:
            coincidences.append(match.group().capitalize())
    
    murderers = ','.join(coincidences)
    return print(murderers)

"Usando filter para mejor implementación"
def find_killer(whisper:str , suspects:list) -> str:
    whisper = whisper.replace('~','\w*')
    pattern = r'{}'.format(whisper)

    coincidences = list(filter(
        lambda suspect: True if re.search(pattern, suspect, re.IGNORECASE) else False,
        suspects))

    murderers = ','.join(coincidence.capitalize() for coincidence in coincidences)

    return print(murderers)

whisper = 'd~~~~~a';
suspects = ['Dracula', 'Freddy Krueger', 'Jason Voorhees', 'Michael Myers'];

find_killer(whisper, suspects); 'Dracula'

whisper2 = '~r~dd~';
suspects2 = ['Freddy', 'Freddier', 'Fredderic']

find_killer(whisper2, suspects2); 'Freddy,Freddier,Fredderic'



whisper = 'd~~~~~a';
suspects = ['Dracula', 'Freddy Krueger', 'Jason Voorhees', 'Michael Myers'];

find_the_killer(whisper, suspects); 'Dracula'

whisper2 = '~r~dd~';
suspects2 = ['Freddy', 'Freddier', 'Fredderic']

find_the_killer(whisper2, suspects2); 'Freddy,Freddier,Fredderic'

whisper3 = '~r~dd$';
suspects3 = ['Freddy', 'Freddier', 'Fredderic']

find_the_killer(whisper3, suspects3); ''

whisper4 = 'mi~~def';
suspects4 = ['Midudev', 'Midu', 'Madeval']

find_the_killer(whisper4, suspects4); ''