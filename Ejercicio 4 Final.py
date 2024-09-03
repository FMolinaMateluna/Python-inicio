#Definimos la clase padre con sus propiedades y devolvemos el saludo inicial
class Persona ():
    def __init__(self, nombre, apellido, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
    def saludar(self):
        print (f"Bienvenido {self.nombre} {self.apellido}")
#Definimos la clase hija de persona, heredando sus propiedades y añadiendo una nueva
class Italiano(Persona):
#El idioma y la nacionalidad siempre seran las mismas
    IDIOMA_PRINCIPAL = "Italiano"
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido, "Italiana")
        self.idioma = Italiano.IDIOMA_PRINCIPAL
# Devolvemos el saludo a la persona
    def saludar(self):
        print (f"Bonjorno! Mi chiamo {self.nombre} {self.apellido} e sono di nazionalità italiana e la mia lingua è italiano")
# Pedimos al usuario que ingrese su nombre y apellido para poder saludarlo
    def datos_usuario():
        nombre = input ("Ingrese su nombre aqui: ")
        apellido = input ("Ingrese su apellido aqui: ")
        return Italiano(nombre,apellido)
persona_italiana = Italiano.datos_usuario()
persona_italiana.saludar()