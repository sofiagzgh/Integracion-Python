### 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
###    con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def diccionario(cadena):
    d = dict()
    for caracter in cadena.upper():
        if caracter != ' ':
            d[caracter] = d.get(caracter, 0) + 1
    return d

# --- PRUEBA 3

cadena_3 = input("Escriba una cadena de caracteres: ")
resultado_3 = diccionario(cadena_3)

print(f"Los caracteres que contiene la cadena '{cadena_3}' son: ")
print(resultado_3)

### 4. Escribir otra función que reciba el diccionario generado con la función anterior
###    y devuelva una tupla con la palabra más repetida y su frecuencia.

def caracter_mas_repetido(dicc):
    return max(dicc, key=dicc.get),max(dicc.values())

# --- PRUEBA 4
resultado_4 = caracter_mas_repetido(resultado_3)
print(f"El caracter mas repetido de la cadena '{cadena_3}' es '{resultado_4[0]}', con {resultado_4[1]} repeticiones.")
