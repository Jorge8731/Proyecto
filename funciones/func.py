import csv

class Residente:
    def __init__(self, id, nombre, edad, genero, habitacion):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.habitacion = habitacion

class Incidencia:
    def __init__(self, id_incidencia, id_residente, fecha, sintomas, diagnostico, tratamiento, estado_actual):
        self.id_incidencia = id_incidencia
        self.id_residente = id_residente
        self.fecha = fecha
        self.sintomas = sintomas
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.estado_actual = estado_actual

class PersonalSalud:
    def __init__(self, id, nombre, especialidad, contacto):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.contacto = contacto

# Funciones para manejar CSV
def leer_residentes(file_path):
    residentes = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            residentes.append(Residente(row['ID'], row['Nombre'], row['Edad'], row['Genero'], row['Habitacion']))
    return residentes

def leer_incidencias(file_path):
    incidencias = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            incidencias.append(Incidencia(row['ID_Incidencia'], row['ID_Residente'], row['Fecha'], row['Sintomas'], row['Diagnostico'], row['Tratamiento'], row['Estado_Actual']))
    return incidencias

def leer_personal_salud(file_path):
    personal_salud = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            personal_salud.append(PersonalSalud(row['ID'], row['Nombre'], row['Especialidad'], row['Contacto']))
    return personal_salud
