#Con list comprehesion
print('list comprehesion: ',[i for i in range(11)])

#Ciclo for
for i in range(11): print(f"ciclo for: {i}")
#Ciclo while
i = 1
while i <= 10: 
    print('ciclo while: ',i)
    i += 1

#Con una función recursiva
def recursiva(num):
    print(f'funcion recursiva: {num}')
    if num == 10: return
    recursiva(num + 1)
recursiva(0)

#Con un iterador y su iterable
lista_numero = [1,2,3,4,5,6,7,8,9,10]
iterador = iter(lista_numero)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

#Con una clase iterador
class iterador():
    def __init__(self, items) -> None:
        self.lista = items
    
    def __iter__(self):
        return iter(self.lista)

objeto_iterable = iterador(lista_numero)
for i in objeto_iterable: print('clase iteradora: ',i) 