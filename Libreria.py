# Tarea 1
# Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, editorial y autor(es). Considerar que un libro puede tener varios autores.

# Se solicita escribir un programa en Python que permita registrar libros. Debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python.

# Dicho programa debe tener un menu (a interactuar en la línea de comando) para:

# Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
# Opción 2: Listar libros.
# Opción 3: Agregar libro.
# Opción 4: Eliminar libro.
# Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
# Opción 6: Ordenar libros por título.
# Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.
# Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.
# Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
# Opción 10: Guardar libros en archivo de disco duro (.txt o csv).
# Nota: listar libros involucra: título, género, ISBN, editorial y autor(es)

#INICIO DE TAREA

from os import system
system("cls")

class libro():

    def __init__(self,id, titulo, genero, ISBN, editorial,autor):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autor = autor
        self.dicc_libros = {} #diccionario vacio

    def menu(self):
        print( "Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.\nOpción 2: Listar libros.\nOpción 3: Agregar libro.\nOpción 4: Eliminar libro.\nOpción 5: Buscar libro por ISBN o por título.\nOpción 6: Ordenar libros por título.\nOpción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.\nOpción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.\nOpción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).\nOpción 10: Guardar libros en archivo de disco duro (.txt o csv).")

"hola como van"
print("hola mundo")

def leer_archivo(self):
    datos = pd.read_csv("libros.csv")
    #print(datos.sort_values(by="id"))
    print(datos.iloc[0:3])
