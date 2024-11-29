"""
Los métodos de instancia son creados para modificar un objeto instanciado de una clase.

Los métodos de clase trabajan directamente con la clase, desde que su parámetro es la clase en sí.

Los métodos estáticos no saben nada acerca de la clase, solo trabajan con los parámetros recibidos.
"""
class MyClass:
    def instance_method(self):
        """ Instance method """
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        """ Class method """
        return 'class method called', cls

    @staticmethod
    def static_method():
        """ Static method """
        return 'static method called'

obj = MyClass()

obj.instance_method()
#>>('instance method called', <__main__.MyClass at 0x10668ea90>)

MyClass.instance_method(obj)
#>>('instance method called', <__main__.MyClass at 0x10668ea90>)

obj.class_method()
#>>('class method called', __main__.MyClass)

obj.static_method()
#>>'static method called'

"Lo que sucede cuando accedemos a los métodos sin instanciar la clase"
MyClass.class_method()
#>>('class method called', __main__.MyClass)

MyClass.static_method()
#>>'static method called'

MyClass.instance_method()
#>>TypeError

"Si que es posible acceder a los métodos de clase y los métodos estáticos sin instanciar la clase, pero para los métodos de intancia si que estamos obligados a instanciar la clase"

# Ejemplos:
"El primer ejemplo va de puros métodos de instancia"
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

#Creamos dos instancias
margherita = Pizza(['mozzarella', 'tomatoes'])
cheese = Pizza(['mozzarella', 'provolone', 'cheddar', 'Parmesan'])

#Gracias al método mágico repr, podemos mandar llamar al objeto así sin más
margherita
#>>Pizza(['mozzarella', 'tomatoes'])

cheese
#>>Pizza(['mozzarella', 'provolone', 'cheddar', 'Parmesan'])

"Ene ste segundo ejemplo vemos que cada instancia puede o no recibir atributos y aún así los métodos de clase ya tienen unos por defecto, gracias a los métodos de clase. Pero, estos métodos de clase no alteran el comportamiento de los objetos instanciados."
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'
    
    def create_custom_pizza(self, ingredients):
        self.ingredients = ingredients
        return self

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def cheese(cls):
        return cls(['mozzarella', 'provolone', 'cheddar', 'Parmesan'])

Pizza.margherita()
#>>Pizza(['mozzarella', 'tomatoes'])

Pizza.cheese()
#>>Pizza(['mozzarella', 'provolone', 'cheddar', 'Parmesan'])

"En los dos casos anteriores vemos que sin instanciar la clase podemos obtenemos un objeto de la clase con atributos específicos."

first_pizza = Pizza([])
first_pizza.ingredients
#>>[]

first_pizza.create_custom_pizza(['chicken', 'mozzarella'])
#>>Pizza(['chicken', 'mozzarella'])

# Podemos mostrar los metodos de clase asociados a la clase Pizza sin cambiar el comportamiento de la instancia
first_pizza.margherita()
#>>Pizza(['mozzarella', 'tomatoes'])

first_pizza.ingredients
#>>['chicken', 'mozzarella']

