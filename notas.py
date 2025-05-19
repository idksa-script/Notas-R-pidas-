import sys 
from pathlib import Path

# Función para dividir el texto en líneas de hasta 15 palabras
def agregar(texto):
    listas = []  # Lista para almacenar las líneas divididas
    for i in range(0, len(texto), 15):  # Iterar cada 15 palabras
        lista = " ".join(texto[i:i+15])  # Unir las palabras en una línea
        listas.append(lista)  # Agregar la línea a la lista
    palabras = "\n".join(listas)  # Combinar las líneas con saltos de línea
    return palabras  # Retornar el texto dividido

# Verificar que se pasen al menos 2 argumentos
if len(sys.argv) < 2:
    print("Debes de agregar por lo menos un argumento")
    exit()  # Terminar el programa si no hay suficientes argumentos

# Ruta donde se guardarán las notas
rutaSave = "/home/idksa_script/Documentos/.Notas/"

# Comprobar el primer argumento para determinar la acción
if sys.argv[1] == "-a":  # Modo agregar texto a un archivo existente
    carpetaArchivo = Path(f"{rutaSave}{sys.argv[2]}.txt")  # Ruta completa del archivo
    if carpetaArchivo.exists():  # Verificar si el archivo existe
        texto = sys.argv[3].split()  # Dividir el texto en palabras
        with open(f"{str(carpetaArchivo)}", "a") as n:  # Abrir el archivo en modo adjuntar
            n.write(agregar(texto) + "\n")  # Escribir el texto formateado
    else:
        print(Path(f"{sys.argv[2]}"))  # Mostrar el nombre del archivo buscado
        print("El archivo no existe")  # Mensaje si el archivo no existe

elif sys.argv[1] == "-v":  # Modo listar archivos
    carpeta = Path(rutaSave)  # Ruta de la carpeta de notas
    print("Archivos encontrados: \n")  # Mensaje inicial
    for archivo in carpeta.iterdir():  # Iterar sobre los archivos en la carpeta
        if archivo.is_file():  # Comprobar si es un archivo
            print(archivo.name)  # Imprimir el nombre del archivo

else:  # Crear un archivo nuevo con texto proporcionado
    texto = sys.argv[1].split()  # Dividir el argumento en palabras
    nombreCompleto = f"{rutaSave}{texto[0]}"  # Crear la ruta completa del archivo

    textoPorlineas = agregar(texto)  # Formatear el texto en líneas de 15 palabras

    with open(f"{nombreCompleto}.txt", "w") as n:  # Abrir el archivo en modo escritura
        n.write(textoPorlineas + "\n")  # Escribir el texto formateado en el archivo

