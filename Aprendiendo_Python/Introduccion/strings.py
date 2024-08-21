#Tipo de dato que almacena cadenas de texto y caracteres, además posee varios métodos interesantes. Los string son inmutables, en tiempo de ejecución no pueden cambiar su valor
nombre_completo = 'Christian Jesus Monroy Gutierrez'

#El método split() puede partir o dividir una cadena de texto, generando una lista con los elementos de la cadena
lista_nombre = nombre_completo.split() #El método split divide por default con espacios, cada espacio en la cadena, es un nuevo elemento

#El método join() genera una cadena apartir de una lista. Quien manda a llamar al método es el caracter que se va a intercalar entre los elementos
nombre_completo = ' '.join(lista_nombre)

#suma de carácteres
nombre = 'Christian'
segundo_nombre = 'Jesus'
nombres = nombre + " " +segundo_nombre

#Para introducir variables en una cadena de texto, se utiliza %s
texto = "Mi nombre es %s %s, %s." %(nombre, segundo_nombre, 'Monroy')

#Usando placeholders y usando el método format, es casi igual a la opción anterior
texto = "Mi nombre es {} {}".format(nombre, segundo_nombre)

#Otra opcion con format. En esta forma se especifica el valor de cada variable y su orden específico
texto = 'Mi nombre es {apellido} {nombre} '.format(nombre = nombre, apellido = "Monroy")

#Otra forma de contatenar texto y variables usando f'', esta forma se pueden interpolar cualquier tipo de dato
texto = f'Mi nombre es {nombre_completo} {10 + 20} {True} {[1, [], False]}'

#Con el método count() como lo dice, cuenta los caracteres o cadena que se le mande como argumento
texto.count('Chris')
#Una forma similar, donde solo queremos saber si se encuentra o no, ya que in retorna un valor booleano
'Chris' in texto

#Existen dos métodos para hacer que las cadenas se encuentren en minúscula y mayúscula
texto.lower()
texto.upper()

#Para justificar o alinear el texto se usan los métodos ljust(), rjust(), center(). No se modifica el texto original, se debe almacenar en una variable lo retornado
texto = texto.ljust(5) #Se recibe como argumento un número, este simboliza la cantidad de espacios que se dejaran de ese lado
texto = texto.rjust(5)
texto = texto.center(10)
