# El i es el elemento

# alumnos = ["Farit", "Javier", "Luis"]

# for i in alumnos:
#    print(i)
# i ++
# 5 < 5

# range ( valor_inicio, valor_fin, contador)
# for i in range(2,11,2):
#    print(i)

# Hola Hola Hola Hola Hola
# print("Hola " * 5 )

# Quiero que mediante un bucle for me impriman en pantalla

# for i in range(1,6):
#    print("T"*i)
# T
# TT
# TTT
# TTTT
# TTTTT

# Cuando pones range SOLO
# Significa que por defecto inicia en el valor de 1
# Termina en el valor señalado  => 4   => 1,2,3,4
# niveles = 4
# # El i => vale = 0
# for i in range(niveles):
#    espacio = " " * (niveles - i -1)
#    letras = "T" * (2 * i + 1)
#    print(espacio + letras)

#    T
#   TTT
# #  TTTTT
# # TTTTTTT


# # POO
# # Paradimga
# #  -Imperativo
# #  -Reactivo
# #  -POO

# # Clase => Es un molde - nosotros la forma que desemos

# # class Animal:
# #    # El constructor son los atributos para crear mi clase
# #    def __init__(self, nombre, tipo):
# #       print(f"Se creo el animal {nombre} {tipo}")

# # firulais = Animal("Firulais", "perro")


# class Auto:
#    # self  -> this
#    def __init__(self, marca, modelo, limite_velocidad):
#       self.marca = marca
#       self.modelo = modelo
#       self.limite_velocidad = limite_velocidad

#    # Metodo = funcion
#    # Funcion que va acelerar de 10 a 10 Km/h hasta llegar al limite
#    # 0
#    # 10
#    # 20
#    # 30
#    def acelerar(self):
#       for i in range(0, self.limite_velocidad, 10):
#          print(i)

# # mercedes = Auto("mercedes", "ZMS", 31)
# # mercedes.acelerar()

# # PILARES DEL POO
# # Abstraccion => En abstraer los metodo y propiedades de un objeto en la vida real y llevarlo a codigo
# # Polimorfismo => Son las distintas formas que puede tomar mi clase
# # Encapsulamiento => Aislar los metodo u objetos
# # Herencia => Consiste en que una clase padre pueda heredar metodos y propiedades a una clase hija

# # tico = Auto("Tico", "QWE-Z", 15)
# # i20 = Auto("Hyundai", "i20", 150)

# class Animal:
#    def __init__(self, especie, edad):
#       self.especie = especie
#       self.edad = edad

#    # Me va indicar que tipo de animal es
#    def describeme(self):
#       print(f"Este animal es de la especie tal {self.especie}")

# class Perro(Animal):
#    #Sobre escribir el constructor
#    # especie - edad - nombre - amigos

#    #Metodo 1
#    # def __init__(self, especie, edad, nombre, amigos):
#    #    self.especie = especie
#    #    self.edad = edad
#    #    self.nombre = nombre
#    #    self.amigos = amigos

#    #Metodo 2
#    def __init__(self, especie, edad, nombre, amigos):
#       super().__init__(especie, edad)
#       self.nombre = nombre
#       self.amigos = amigos

#    def ladrar(self):
#       print("GUAU GUAU")

# firulais = Perro("canino", 10, "Firulais", "Blanquita")
# print(firulais.edad)

class Auto:

    def __init__(self, modelo, limite):
        self.modelo = modelo
        self.limite = limite
        self.velocidad = 0

    def acelerar(self):
        if self.velocidad >= self.limite:
            print("Llegaste al limite, SUTRAN")
        else:
            self.velocidad = self.velocidad + 10
            print(f"velocidad : {self.velocidad} ")

dd = Auto("vw", 20)
dd.acelerar()
dd.acelerar()
dd.acelerar()
