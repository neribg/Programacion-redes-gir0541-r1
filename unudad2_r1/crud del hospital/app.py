import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Establece la conexión con la base de datos
def get_db_connection():
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un paciente por ID
@app.route('/pacientes', methods=['GET'])
def query_pacientes():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Pacientes')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método PUT donde crea un paciente
@app.route('/pacientes', methods=['PUT'])
def create_paciente():
    paciente = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO Pacientes (idPaciente, nombre, apellido, edad, sexo, fechaNacimiento, domicilio, telefono) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, (paciente['idPaciente'], paciente['nombre'], paciente['apellido'], paciente['edad'], paciente['sexo'], paciente['fechaNacimiento'], paciente['domicilio'], paciente['telefono']))
    conn.commit()
    return jsonify(paciente)

# Método DELETE donde elimina un paciente por ID
@app.route('/pacientes', methods=['DELETE'])
def delete_paciente():
    paciente = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Pacientes WHERE idPaciente = ?'
    cursor.execute(delete, (paciente['idPaciente'],))
    conn.commit()
    return jsonify(paciente)

# Método POST donde actualiza un paciente por ID
@app.route('/pacientes', methods=['POST'])
def update_paciente():
    paciente = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE Pacientes SET nombre = ?, apellido = ?, edad = ?, sexo = ?, fechaNacimiento = ?, domicilio = ?, telefono = ? WHERE idPaciente = ?'
    cursor.execute(update, (paciente['nombre'], paciente['apellido'], paciente['edad'], paciente['sexo'], paciente['fechaNacimiento'], paciente['domicilio'], paciente['telefono'], paciente['idPaciente']))
    conn.commit()
    return jsonify(paciente)

# Método GET donde busca una historia clínica por ID
@app.route('/historiasclinicas', methods=['GET'])
def query_historiasclinicas():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM HistoriaClinica')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método PUT donde crea una historia clínica
@app.route('/historiasclinicas', methods=['PUT'])
def create_historiaclinica():
    historiaclinica = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO HistoriaClinica (idHistoriaClinica, idPaciente, fechaConsulta, motivoConsulta, diagnostico, tratamiento, observaciones) VALUES (?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(insert, (historiaclinica['idHistoriaClinica'], historiaclinica['idPaciente'], historiaclinica['fechaConsulta'], historiaclinica['motivoConsulta'], historiaclinica['diagnostico'], historiaclinica['tratamiento'], historiaclinica['observaciones']))
    conn.commit()
    return jsonify(historiaclinica)

# Método DELETE donde elimina una historia clínica por ID
@app.route('/historiasclinicas', methods=['DELETE'])
def delete_historiaclinica():
    historiaclinica = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM HistoriaClinica WHERE idHistoriaClinica = ?'
    cursor.execute(delete, (historiaclinica['idHistoriaClinica'],))
    conn.commit()
    return jsonify(historiaclinica)

# Método POST donde actualiza una historia clínica por ID
@app.route('/historiasclinicas', methods=['POST'])
def update_historiaclinica():
    historiaclinica = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE HistoriaClinica SET idPaciente = ?, fechaConsulta = ?, motivoConsulta = ?, diagnostico = ?, tratamiento = ?, observaciones = ? WHERE idHistoriaClinica = ?'
    cursor.execute(update, (historiaclinica['idPaciente'], historiaclinica['fechaConsulta'], historiaclinica['motivoConsulta'], historiaclinica['diagnostico'], historiaclinica['tratamiento'], historiaclinica['observaciones'], historiaclinica['idHistoriaClinica']))
    conn.commit()
    return jsonify(historiaclinica)

# Verifica el nombre e inicia el servicio
if __name__ == '__main__':
    app.run(debug=True)
