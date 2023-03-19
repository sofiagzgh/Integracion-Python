### 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
###    cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
###    del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
###    ejercicio tanto de manera iterativa como recursiva.

# Función iterativa:

def get_int():
    while True:
        try:
            user_value = int(input("1. Ingrese un numero entero: "))
            return user_value
        except ValueError:
            print("El numero ingresado no es entero. Intente nuevamente.")
get_int()

# Función recursiva:

def get_int():
    try:
        user_value = int(input("2. Ingrese un numero entero: "))
        return user_value
    except ValueError:
        print("El numero ingresado no es entero. Intente nuevamente.")
        return get_int()
get_int()