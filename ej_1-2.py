import math


# 1. Escribir una función que calcule el máximo común divisor entre dos números.

def maximo_comun_divisor(a, b):
    # para que tome parametros iguales a cero
    if a == 0 or b == 0:
        return a + b
    # para que tome parametros iguales entre si
    elif a == b:
        return a
    else:
        # para que tome parametros negativos
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        # para que "a" sea el mayor numero de los dos parametros ingresados
        if b > a:
            a, b = b, a
        # calculo
        while a % b != 0:
            b, a = a % b, b
        return b

# --- PRUEBA 1


num1 = int(input("Ingrese un primer numero entero: "))
num2 = int(input("Ingrese un segundo numero entero: "))

resultado_1 = maximo_comun_divisor(num1, num2)
chequeo_1 = math.gcd(num1, num2)
print("----------------------------------------------------------")
print(f"El Máximo Común divisor de {num1} y {num2} es {resultado_1}.")
print('Chequeo con math:', chequeo_1)
print("----------------------------------------------------------")


# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def minimo_comun_multiplo(a, b):
    return int((a*b)/maximo_comun_divisor(a, b))

# --- PRUEBA 2


resultado_2 = minimo_comun_multiplo(num1, num2)
chequeo_2 = math.lcm(num1, num2)

print(f"El Mínimo común múltiplo de {num1} y {num2} es {resultado_2}.")
print('Chequeo con math:', chequeo_2)
print("----------------------------------------------------------")
