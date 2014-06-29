## DECORATOR PARA LA VERICACION DE EXISTENCIA DE UN USUARIO
## EN FUNCION Y EN CLASE
"""
from functools import wraps
def verificar_usuario(dni):
	def decorator(function):
		def inner_decorator(*args, **kwargs):
			lista_dni = [45561659, 20116552]
			if lista_dni.__contains__(dni):
				return function(*args, **kwargs)
			else:
				print 'Este usuario no esta registrado'
		return wraps(function)(inner_decorator)
	return decorator

class VerificarDni:
	def __init__(self, dni):
		self.dni = dni
		self.lista_dni = [20116552, 45561659]
			
	def __call__(self, function):
		self.funcion = function
		from functools import wraps
		def inner_decorator(*args, **kwargs):
			if self.lista_dni.__contains__(self.dni):
				print 'Unlocked'
				return self.funcion(*args, **kwargs)
			else:
				print 'Locked'
		return wraps(self.funcion)(inner_decorator)
	
#@verificar_usuario(20)
@VerificarDni(20116551)
def prueba(cadena):
	print cadena

prueba("asdf")
"""

# print '{:,}'.format(123456789.5)  ##Separador de miles
# print 	max(range(1,5))

""" 
## Ejemplos de map 
def saludar(lang):
	if lang == "es":
		print "Hola"
	if lang == "en":
		print "Welcome"
	if lang == "fr":
		print "Salut"

lista_opciones = ["fr","es","en"]
map(saludar, lista_opciones)

"""
# print pow(2,3) # Funcion potencia 

# print reduce(lambda x, y: x +y, range(1,6))

a = set(range(1,6))
print a, type(a)