import json

def cargar_datos(archivo):
    with open (archivo) as contenido:
      libros= json.load(contenido);
      for libros in libros:
         print(libros.get('name'));
        





if __name__ =='__main__':
    archivo ='libros.json'
    cargar_datos(archivo)
    