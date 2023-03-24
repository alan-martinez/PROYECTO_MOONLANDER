from flask import Flask, request
import csv

app = Flask(__name__)

@app.route('/guardar_datos', methods=['POST'])
def guardar_datos():
    datos = request.json['datos']
    with open('datos_entrenamiento.csv', 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(datos)
    return 'OK'

if __name__ == '__main__':
    app.run(port=8000)
