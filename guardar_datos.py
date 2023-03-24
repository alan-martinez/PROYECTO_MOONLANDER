import csv

def guardar_datos(altura, velocidad, combustible):
    with open('datos_nave.csv', mode='a') as archivo_datos:
        datos_escritor = csv.writer(archivo_datos, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        datos_escritor.writerow([altura, velocidad, combustible])
