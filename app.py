from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import config

app = Flask(__name__)
app.config.from_object(config.Config)

mysql = MySQL(app)

@app.route('/registros', methods=['GET'])
def get_registros():
    # Parámetros de paginación
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    
    if page < 1:
        page = 1
    if per_page < 1:
        per_page = 10
    
    offset = (page - 1) * per_page
    
    cur = mysql.connection.cursor()
    
    # Contar el número total de registros
    cur.execute("SELECT COUNT(*) FROM registros")
    total_records = cur.fetchone()[0]
    
    # Obtener los registros de la página actual
    cur.execute("SELECT * FROM registros LIMIT %s OFFSET %s", (per_page, offset))
    rows = cur.fetchall()
    cur.close()
    
    registros = []
    for row in rows:
        registros.append({
            'id_registro': row[0],
            'estado': row[1],
            'id': row[2],
            'matricula': row[3],
            'razon_social': row[4],
            'cod_estado_actualizacion': row[5],
            'cod_departamento': row[6],
            'id_establecimiento': row[7],
            'direccion': row[8],
            'respuesta_json': row[9],
            'fecha_insercion': row[10]
        })
    
    # Calcular el total de páginas
    total_pages = (total_records + per_page - 1) // per_page
    
    response = {
        'page': page,
        'per_page': per_page,
        'total_records': total_records,
        'total_pages': total_pages,
        'registros': registros
    }
    
    return jsonify(response)

@app.route('/registros/<int:id_registro>', methods=['GET'])
def get_registro(id_registro):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM registros WHERE id_registro = %s", (id_registro,))
    row = cur.fetchone()
    cur.close()
    
    if row:
        registro = {
            'id_registro': row[0],
            'estado': row[1],
            'id': row[2],
            'matricula': row[3],
            'razon_social': row[4],
            'cod_estado_actualizacion': row[5],
            'cod_departamento': row[6],
            'id_establecimiento': row[7],
            'direccion': row[8],
            'respuesta_json': row[9],
            'fecha_insercion': row[10]
        }
        return jsonify(registro)
    else:
        return jsonify({'error': 'Registro no encontrado'}), 404

@app.route('/registros', methods=['POST'])
def create_registro():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO registros (estado, id, matricula, razon_social, cod_estado_actualizacion, cod_departamento, id_establecimiento, direccion, respuesta_json)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (data['estado'], data['id'], data['matricula'], data['razon_social'], data['cod_estado_actualizacion'], data['cod_departamento'], data['id_establecimiento'], data['direccion'], data['respuesta_json']))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Registro creado exitosamente'}), 201

@app.route('/registros/<int:id_registro>', methods=['PUT'])
def update_registro(id_registro):
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE registros
        SET estado = %s, id = %s, matricula = %s, razon_social = %s, cod_estado_actualizacion = %s, cod_departamento = %s, id_establecimiento = %s, direccion = %s, respuesta_json = %s
        WHERE id_registro = %s
    """, (data['estado'], data['id'], data['matricula'], data['razon_social'], data['cod_estado_actualizacion'], data['cod_departamento'], data['id_establecimiento'], data['direccion'], data['respuesta_json'], id_registro))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Registro actualizado exitosamente'})

@app.route('/registros/<int:id_registro>', methods=['DELETE'])
def delete_registro(id_registro):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM registros WHERE id_registro = %s", (id_registro,))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Registro eliminado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)
