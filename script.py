import yaml

def mostrar_contenido_yml(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = yaml.safe_load(archivo)
        print(yaml.dump(contenido, default_flow_style=False))

if __name__ == "__main__":
    ruta_archivo = '.github/workflows/c-cpp.yml'
    mostrar_contenido_yml(ruta_archivo)