"""
Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

def palabras():
    def palindromo(palabra1:str, palabra2: str):
        if palabra1 == palabra1[::-1]:
            print(f"{palabra1 } Es palíndromo")
        else:
            print(f"{palabra1} No es palíndromo")

        print(f"¿{palabra2} es un palindomo? {palabra2 == palabra2[::-1]}")


    def anagrama(palabra1:str, palabra2:str):
        print(f"¿{palabra1} es un anagrama de {palabra2}?  {sorted(palabra1) == sorted(palabra2)}")    


    def isograma(palabra1:str):
        dicc = dict()
        for letra in palabra1:
            dicc[letra] = dicc.get(letra,0) + 1

        es_isograma = True
        valores = list(dicc.values())
        longitud_dicc = valores[0]
        for i in valores:
            if i != longitud_dicc:
                es_isograma = False
                break

        print(f"¿{palabra1} es un isograma? {es_isograma}")



    palindromo("caca", "anitalavalatina")
    anagrama("alberca", "cazuela")
    isograma("acondicionar")
palabras()