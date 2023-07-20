from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk

from models import Evento, RutaVisita, Ubicacion, Usuario, Review, DataReader


class EventosApp:
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry("600x400")
        self.app.configure(bg="#2F242C")  # Color de fondo principal

        self.purpura_oscuro = "#2F242C"
        self.gris_claro = "#E5E5E5"
        self.amarillo = "#E6D884"
        self.verde_claro = "#A1A892"

        self.eventos = []
        self.rutas = []
        self.ubicaciones = []
        self.usuarios = []
        self.reviews = []

        self.eventos_listbox = None
        self.rutas_listbox = None
        self.ubicaciones_listbox = None
        self.usuarios_listbox = None
        self.reviews_listbox = None

        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        try:
            self.eventos = self.load_eventos_from_file('eventos.json')
            self.rutas = self.load_rutas_from_file('rutas.json')
            self.ubicaciones = self.load_ubicaciones_from_file('ubicaciones.json')
            self.usuarios = self.load_usuarios_from_file('usuarios.json')
            self.reviews = self.load_reviews_from_file('reviews.json')
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_eventos_from_file(self, file_path):
        eventos_data = DataReader.load_data_from_file(file_path)
        eventos = []
        for evento_data in eventos_data:
            evento = Evento(
                evento_data['id'], evento_data['nombre'], evento_data['artista'],
                evento_data['genero'], evento_data['id_ubicacion'], evento_data['hora_inicio'],
                evento_data['hora_fin'], evento_data['descripcion'], evento_data['imagen']
            )
            eventos.append(evento)
        return eventos

    def load_rutas_from_file(self, file_path):
        rutas_data = DataReader.load_data_from_file(file_path)
        rutas = []
        for ruta_data in rutas_data:
            ruta = RutaVisita(ruta_data['id'], ruta_data['nombre'], ruta_data['destinos'])
            rutas.append(ruta)
        return rutas

    def load_ubicaciones_from_file(self, file_path):
        ubicaciones_data = DataReader.load_data_from_file(file_path)
        ubicaciones = []
        for ubicacion_data in ubicaciones_data:
            ubicacion = Ubicacion(
                ubicacion_data['id'], ubicacion_data['nombre'], ubicacion_data['direccion'],
                ubicacion_data['coordenadas']
            )
            ubicaciones.append(ubicacion)
        return ubicaciones

    def load_usuarios_from_file(self, file_path):
        usuarios_data = DataReader.load_data_from_file(file_path)
        usuarios = []
        for usuario_data in usuarios_data:
            usuario = Usuario(
                usuario_data['id'], usuario_data['nombre'], usuario_data['apellido'],
                usuario_data['historial_eventos']
            )
            usuarios.append(usuario)
        return usuarios

    def load_reviews_from_file(self, file_path):
        reviews_data = DataReader.load_data_from_file(file_path)
        reviews = []
        for review_data in reviews_data:
            review = Review(
                review_data['id'], review_data['id_evento'], review_data['id_usuario'],
                review_data['calificacion'], review_data['comentario'], review_data['animo']
            )
            reviews.append(review)
        return reviews

    def mostrar_detalles_evento(self, evento):
        messagebox.showinfo(
            "Detalles del Evento",
            f"Nombre: {evento.nombre}\nArtista: {evento.artista}\nGénero: {evento.genero}\n"
            f"Ubicación: {evento.id_ubicacion}\nHora de Inicio: {evento.hora_inicio}\n"
            f"Hora de Fin: {evento.hora_fin}\nDescripción: {evento.descripcion}"
        )

    def evento_seleccionado(self, event):
        selected_item = self.eventos_listbox.get(event.widget.curselection())
        evento = self.obtener_evento_por_nombre(selected_item)
        if evento:
            self.mostrar_detalles_evento(evento)

    def obtener_evento_por_nombre(self, nombre):
        for evento in self.eventos:
            if evento.nombre == nombre:
                return evento
        return None

    def cargar_lista_eventos(self):
        self.eventos_listbox.delete(0, tk.END)
        for evento in self.eventos:
            self.eventos_listbox.insert(tk.END, evento.nombre)

    def filtrar_eventos(self):
        nombre = self.nombre_entry.get()
        genero = self.genero_entry.get()
        artista = self.artista_entry.get()
        ubicacion = self.ubicacion_combobox.get()
        hora_inicio = self.hora_inicio_entry.get()
        hora_fin = self.hora_fin_entry.get()

        eventos_filtrados = []

        for evento in self.eventos:
            if nombre and nombre.lower() not in evento.nombre.lower():
                continue
            if genero and genero.lower() not in evento.genero.lower():
                continue
            if artista and artista.lower() not in evento.artista.lower():
                continue
            if ubicacion and ubicacion != evento.id_ubicacion:
                continue
            if hora_inicio and hora_inicio > evento.hora_inicio:
                continue
            if hora_fin and hora_fin < evento.hora_fin:
                continue

            eventos_filtrados.append(evento)

        self.cargar_lista_eventos_filtrados(eventos_filtrados)

    def cargar_lista_eventos_filtrados(self, eventos_filtrados):
        self.eventos_listbox.delete(0, tk.END)
        for evento in eventos_filtrados:
            self.eventos_listbox.insert(tk.END, evento.nombre)

    def abrir_archivo_eventos(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filepath:
            try:
                with open(filepath, 'r') as file:
                    eventos_data = json.load(file)
                with open('eventos.json', 'w') as file:
                    json.dump(eventos_data, file)
                self.cargar_datos_iniciales()
                self.cargar_lista_eventos()
            except Exception as e:
                messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

    def abrir_archivo_rutas(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filepath:
            try:
                with open(filepath, 'r') as file:
                    rutas_data = json.load(file)
                with open('rutas.json', 'w') as file:
                    json.dump(rutas_data, file)
                self.cargar_datos_iniciales()
                self.cargar_lista_rutas()
            except Exception as e:
                messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

    def abrir_archivo_ubicaciones(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filepath:
            try:
                with open(filepath, 'r') as file:
                    ubicaciones_data = json.load(file)
                with open('ubicaciones.json', 'w') as file:
                    json.dump(ubicaciones_data, file)
                self.cargar_datos_iniciales()
                self.cargar_lista_ubicaciones()
            except Exception as e:
                messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

    def abrir_archivo_usuarios(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filepath:
            try:
                with open(filepath, 'r') as file:
                    usuarios_data = json.load(file)
                with open('usuarios.json', 'w') as file:
                    json.dump(usuarios_data, file)
                self.cargar_datos_iniciales()
                self.cargar_lista_usuarios()
            except Exception as e:
                messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

    def abrir_archivo_reviews(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filepath:
            try:
                with open(filepath, 'r') as file:
                    reviews_data = json.load(file)
                with open('reviews.json', 'w') as file:
                    json.dump(reviews_data, file)
                self.cargar_datos_iniciales()
                self.cargar_lista_reviews()
            except Exception as e:
                messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

    def mostrar_detalles_ubicacion(self, ubicacion):
        messagebox.showinfo(
            "Detalles de la Ubicación",
            f"Nombre: {ubicacion.nombre}\nDirección: {ubicacion.direccion}\n"
            f"Coordenadas: {ubicacion.coordenadas}"
        )

    def ubicacion_seleccionada(self, event):
        selected_item = self.ubicaciones_listbox.get(event.widget.curselection())
        ubicacion = self.obtener_ubicacion_por_nombre(selected_item)
        if ubicacion:
            self.mostrar_detalles_ubicacion(ubicacion)

    def obtener_ubicacion_por_nombre(self, nombre):
        for ubicacion in self.ubicaciones:
            if ubicacion.nombre == nombre:
                return ubicacion
        return None

    def cargar_lista_rutas(self):
        self.rutas_listbox.delete(0, tk.END)
        for ruta in self.rutas:
            self.rutas_listbox.insert(tk.END, ruta.nombre)

    def cargar_lista_ubicaciones(self):
        self.ubicaciones_listbox.delete(0, tk.END)
        for ubicacion in self.ubicaciones:
            self.ubicaciones_listbox.insert(tk.END, ubicacion.nombre)

    def cargar_lista_usuarios(self):
        self.usuarios_listbox.delete(0, tk.END)
        for usuario in self.usuarios:
            self.usuarios_listbox.insert(tk.END, f"{usuario.nombre} {usuario.apellido}")

    def cargar_lista_reviews(self):
        self.reviews_listbox.delete(0, tk.END)
        for review in self.reviews:
            evento = self.obtener_evento_por_id(review.id_evento)
            usuario = self.obtener_usuario_por_id(review.id_usuario)
            if evento and usuario:
                self.reviews_listbox.insert(tk.END, f"Evento: {evento.nombre} - Usuario: {usuario.nombre}")

    def obtener_evento_por_id(self, evento_id):
        for evento in self.eventos:
            if evento.id == evento_id:
                return evento
        return None

    def obtener_usuario_por_id(self, usuario_id):
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    app = EventosApp()
    app.run()
