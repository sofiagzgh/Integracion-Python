### 6. Crear una clase llamada Persona.
###    Sus atributos son: nombre, edad y DNI.
###    Construya los siguientes métodos para la clase:
###     Un constructor, donde los datos pueden estar vacíos.
###     Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
###     mostrar(): Muestra los datos de la persona.
###     Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():
     # Constructor
     def __intit__(self, nombre = 'Nombre', edad = 0, dni = 0):
            self._nombre = nombre
            self._edad = edad
            self._dni = dni

    # Getters
     def get_nombre(self):
          return self._nombre

     def get_edad(self):
          return self._edad

     def get_dni(self):
          return self._dni

    #  Setters
     def set_nombre(self, nombre):
           if nombre.isalpha():
                 self._nombre = nombre
           else:
                print("El nombre ingresado debe ser una cadena de texto.")

     def set_edad(self, edad):
           if type(edad) == int and edad > 0:
                 self._edad = edad
           else:
                print("La edad ingresada debe ser un numero natural (entero positivo).")

     def set_dni(self, dni):
            if type(dni) == int and dni > 0:
                 self._dni = dni
            else:
                print("El DNI ingresado no debe incluir puntos ni texto.")

    # Metodos
     def mostrar(self):
          print(f"Nombre: {self._nombre.capitalize()},\nEdad: {self._edad} años,\nD.N.I.: {self._dni}.")

     def es_mayor_de_edad(self):
          return self._edad >= 18

# --- PRUEBA 6
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
dni = int(input("Ingrese su DNI: "))

p1 = Persona()
p1.set_nombre(nombre)
p1.set_edad(edad)
p1.set_dni(dni)
print("---------------------6---------------------")
p1.mostrar()
print("¿Es mayor de edad?:", p1.es_mayor_de_edad())


### 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos:
###     titular (que es una persona) y cantidad (puede tener decimales).
###    El titular será obligatorio y la cantidad es opcional.
###    Crear los siguientes métodos para la clase:
###     Un constructor, donde los datos pueden estar vacíos.
###     Los setters y getters para cada uno de los atributos.
###     El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
###     mostrar(): Muestra los datos de la cuenta.
###     ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
###     retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta():
    # Constructor
    def  __init__(self, titular = Persona(), cantidad = 0):
        self._titular = titular
        self._cantidad = cantidad

    # Getters
    def get_titular(self):
       return self._titular

    def get_cantidad(self):
        return self._cantidad

    # Setters
    def set_titular(self, titular):
        self._titular = titular

    # def set_cantidad(self,cantidad):
    #     self.set_cantidad = cantidad

    # Metodos
    def mostrar(self):
        print(f"La cuenta a nombre de {self._titular._nombre.capitalize()} tiene un saldo de ${self._cantidad}")

    def retirar(self, cant):
        if cant >= 0:
             self._cantidad -= cant
             print(f"Se retiraron ${cant}")
        return self._cantidad

    def ingresar(self, cant):
        if cant >= 0:
             self._cantidad += cant
             print(f"Se ingresaron ${cant}")
        return self._cantidad

# --- PRUEBA 7

cta = Cuenta()
cta.set_titular(p1)
print("---------------------7---------------------")
cta.ingresar(1000)
cta.retirar(400)
cta.mostrar()


### 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva
###    de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe
###    guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
###     Un constructor.
###     Los setters y getters para el nuevo atributo.
###     En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear
###     un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años
###     y falso en caso contrario.
###     Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
###     El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class CuentaJoven(Cuenta):
    # Constructor
    def __init__(self, titular, cantidad = 0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    # Getters
    def get_bonificacion(self):
       return self._bonificacion

    # Setters
    def set_bonificacion(self, bonificacion):
        if type(bonificacion) == int or type(bonificacion) == float and bonificacion>=0 and bonificacion<=100:
            self._bonificacion = bonificacion
        else:
             print("Porcentaje invalido de bonificacion")

    # Metodos
    def mostrar(self):
        print(f"Cuenta Joven de {self._titular._nombre.capitalize()}. Bonificacion del {self._bonificacion} %.")

    def es_titular_valido(self):
        return self.get_titular().es_mayor_de_edad() and self.get_titular()._edad < 25

    def retirar(self, cant):
       if self.es_titular_valido():
            super().retirar(cant)
       else:
            print("Titular no valido para la operacion.")

# --- PRUEBA 8

ctajoven= CuentaJoven(p1)
ctajoven.set_bonificacion(80)
print("---------------------8---------------------")
ctajoven.ingresar(100)
ctajoven.retirar(50)
ctajoven.mostrar()