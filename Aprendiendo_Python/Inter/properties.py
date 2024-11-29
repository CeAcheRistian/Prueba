# Las properties son la forma pythonica de evitar la creación de métodos para obtener y modificar atributos de una clase. Esta función nos ayuda a convertir atributos de una clase en properties o managed attributes.
# Hay dos manera de implementarlo, la primera y mejor, con decoradores
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Radius property."""
        print("Get radius")
        return self._radius
    
    @radius.setter
    def radius(self, value):
        print("Set radius")

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius

"Con las properties podemos acceder a los atributos de la clase sin necesidad de crear mil métodos para cada uno de los atributos."

# La segunda manera de hacer esto es así con un objeto que sea instancia de la función property y dentro mandamos a llamar a las funciones de la clase:
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )

"""Para ambos casos: para acceder a estos solo intanciamos la clase y llamamos"""
circle = Circle(10)
circle.radius
circle.radius = 50
del circle.radius

"Atributos de solo lectura"
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
"Atributos de solo escritura"
import hashlib
import os

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Password is write-only")

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_000
        )

"Los properties sirven para validar datos"
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"y" must be a number') from None

point = Point(1,2) # >> Validated!
point.x = "Hola"# >> ValueError

"Atributos que requieren un calculo"
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height