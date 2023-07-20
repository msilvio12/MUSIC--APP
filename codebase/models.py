import json


class Evento:
    def __init__(self, id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

    def __str__(self):
        return f"Evento: {self.nombre} - Artista: {self.artista}"


class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def __str__(self):
        return f"Ruta de Visita: {self.nombre}"


class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    def __str__(self):
        return f"Ubicación: {self.nombre}"


class Usuario:
    def __init__(self, id, nombre, apellido, historial_eventos):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = historial_eventos

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}"


class Review:
    def __init__(self, id, id_evento, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def __str__(self):
        return f"Review: ID Evento={self.id_evento}, ID Usuario={self.id_usuario}"


class DataReader:
    @staticmethod
    def load_data_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            raise Exception(f"No se encontró el archivo '{file_path}'")
        except Exception as e:
            raise Exception(f"Error al cargar los datos del archivo '{file_path}': {str(e)}")
