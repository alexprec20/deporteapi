import os
import json
from flask import Flask, jsonify

# Crear carpeta data si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Generar datos de 10 productos
datos_productos = [
    {"id": "00001", "nombre": "Creatina", "precio": 29.99, "unidades": 100, "stock": "50"},
    {"id": "00002", "nombre": "Proteína Whey", "precio": 45.50, "unidades": 80, "stock": "40"},
    {"id": "00003", "nombre": "BCAA", "precio": 19.99, "unidades": 120, "stock": "60"},
    {"id": "00004", "nombre": "Pre-entreno", "precio": 35.00, "unidades": 50, "stock": "25"},
    {"id": "00005", "nombre": "Multivitamínico", "precio": 15.25, "unidades": 200, "stock": "100"},
    {"id": "00006", "nombre": "Omega 3", "precio": 12.90, "unidades": 150, "stock": "75"},
    {"id": "00007", "nombre": "Magnesio", "precio": 9.99, "unidades": 100, "stock": "50"},
    {"id": "00008", "nombre": "Glutamina", "precio": 22.45, "unidades": 90, "stock": "45"},
    {"id": "00009", "nombre": "Cinturón gym", "precio": 25.00, "unidades": 30, "stock": "15"},
    {"id": "00010", "nombre": "Guantes", "precio": 14.50, "unidades": 40, "stock": "20"}
]

# Crear el fichero productos.json
with open('data/productos.json', 'w', encoding='utf-8') as f:
    json.dump(datos_productos, f, indent=4, ensure_ascii=False)

# Creación de la aplicación Flask
app = Flask(__name__)

# Definición de la ruta (/productos) con un método GET
@app.route('/productos', methods=['GET'])
def obtener_productos():
    # 1. Obtener la ruta absoluta del directorio donde se encuentra este archivo app.py
    directorio_base = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Construir la ruta absoluta hacia el archivo JSON dentro de la carpeta 'data'
    ruta_json = os.path.join(directorio_base, 'data', 'productos.json')
    
    # 3. Leer los datos del archivo JSON
    try:
        with open(ruta_json, 'r', encoding='utf-8') as f:
            productos = json.load(f)
        return jsonify(productos)
    except FileNotFoundError:
        return jsonify({"error": "El archivo de productos no fue encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
