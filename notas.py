import sys 
from pathlib import Path

def agregar(texto):
    listas = []
    for i in range(0, len(texto), 15):
        lista = " ".join(texto[i:i+15])
        listas.append(lista)
    palabras = "\n".join(listas)
    return palabras

if len(sys.argv) < 2:
    print("Debes de argregar por lo menos un argumento")
    exit()

rutaSave = "/home/idksa_script/Documentos/.Notas/"

if sys.argv[1] == "-a":
    carpetaArchivo = Path(f"{rutaSave}{sys.argv[2]}.txt")
    if carpetaArchivo.exists():
        texto = sys.argv[3].split()
        with open(f"{str(carpetaArchivo)}", "a") as n:
            n.write(agregar(texto) + "\n")
    else:
        print(Path(f"{sys.argv[2]}"))
        print("El archivo no existe")

elif sys.argv[1] == "-v":
    carpeta = Path(rutaSave)
    print("Archivos encontrados: \n")
    for archivo in carpeta.iterdir():
        if archivo.is_file():
            print(archivo.name)

else:
    texto = sys.argv[1].split()
    nombreCompleto = f"{rutaSave}{texto[0]}"

    textoPorlineas = agregar(texto)

    with open(f"{nombreCompleto}.txt", "w") as n:
        n.write(textoPorlineas + "\n")
