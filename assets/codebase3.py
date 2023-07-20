import json
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage

# Colores personalizados
purpura_oscuro = "#2F242C"
gris_claro = "#E5E5E5"
amarillo = "#E6D884"
verde_claro = "#A1A892"


app = tk.Tk()
app.geometry("600x400")
app.configure(bg=purpura_oscuro)  # Color de fondo principal

# Definición de la clase Evento
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

# Definición de la clase RutaVisita
class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def __str__(self):
        return f"Ruta de Visita: {self.nombre}"

# Definición de la clase Ubicacion
class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    def __str__(self):
        return f"Ubicación: {self.nombre}"

# Definición de la clase Usuario
class Usuario:
    def __init__(self, id, nombre, apellido, historial_eventos):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = historial_eventos

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}"

# Definición de la clase Review
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

# Función para cargar los eventos desde un archivo JSON
def cargar_eventos():
    try:
        with open('eventos.json', 'r') as file:
            eventos_data = json.load(file)
        eventos = []
        for evento_data in eventos_data:
            evento = Evento(evento_data['id'], evento_data['nombre'], evento_data['artista'],
                            evento_data['genero'], evento_data['id_ubicacion'], evento_data['hora_inicio'],
                            evento_data['hora_fin'], evento_data['descripcion'], evento_data['imagen'])
            eventos.append(evento)
        return eventos
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo 'eventos.json'")
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar los eventos: {str(e)}")
    return []

# Función para cargar las rutas de visita desde un archivo JSON
def cargar_rutas():
    try:
        with open('rutas.json', 'r') as file:
            rutas_data = json.load(file)
        rutas = []
        for ruta_data in rutas_data:
            ruta = RutaVisita(ruta_data['id'], ruta_data['nombre'], ruta_data['destinos'])
            rutas.append(ruta)
        return rutas
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo 'rutas.json'")
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar las rutas de visita: {str(e)}")
    return []

# Función para cargar las ubicaciones desde un archivo JSON
def cargar_ubicaciones():
    try:
        with open('ubicaciones.json', 'r') as file:
            ubicaciones_data = json.load(file)
        ubicaciones = []
        for ubicacion_data in ubicaciones_data:
            ubicacion = Ubicacion(ubicacion_data['id'], ubicacion_data['nombre'], ubicacion_data['direccion'],
                                  ubicacion_data['coordenadas'])
            ubicaciones.append(ubicacion)
        return ubicaciones
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo 'ubicaciones.json'")
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar las ubicaciones: {str(e)}")
    return []

# Función para cargar los usuarios desde un archivo JSON
def cargar_usuarios():
    try:
        with open('usuarios.json', 'r') as file:
            usuarios_data = json.load(file)
        usuarios = []
        for usuario_data in usuarios_data:
            usuario = Usuario(usuario_data['id'], usuario_data['nombre'], usuario_data['apellido'],
                              usuario_data['historial_eventos'])
            usuarios.append(usuario)
        return usuarios
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo 'usuarios.json'")
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar los usuarios: {str(e)}")
    return []

# Función para cargar las reviews desde un archivo JSON
def cargar_reviews():
    try:
        with open('reviews.json', 'r') as file:
            reviews_data = json.load(file)
        reviews = []
        for review_data in reviews_data:
            review = Review(review_data['id'], review_data['id_evento'], review_data['id_usuario'],
                            review_data['calificacion'], review_data['comentario'], review_data['animo'])
            reviews.append(review)
        return reviews
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo 'reviews.json'")
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar las reviews: {str(e)}")
    return []

# Función para mostrar los detalles de un evento seleccionado
def mostrar_detalles_evento(evento):
    messagebox.showinfo("Detalles del Evento",
                        f"Nombre: {evento.nombre}\nArtista: {evento.artista}\nGénero: {evento.genero}\n"
                        f"Ubicación: {evento.id_ubicacion}\nHora de Inicio: {evento.hora_inicio}\n"
                        f"Hora de Fin: {evento.hora_fin}\nDescripción: {evento.descripcion}")

# Función para manejar el evento de clic en un evento de la lista
def evento_seleccionado(event):
    selected_item = eventos_listbox.get(event.widget.curselection())
    evento = obtener_evento_por_nombre(selected_item)
    if evento:
        mostrar_detalles_evento(evento)

# Función para obtener un evento por su nombre
def obtener_evento_por_nombre(nombre):
    for evento in eventos:
        if evento.nombre == nombre:
            return evento
    return None

# Función para cargar la lista de eventos en el widget ListBox
def cargar_lista_eventos():
    eventos_listbox.delete(0, tk.END)
    for evento in eventos:
        eventos_listbox.insert(tk.END, evento.nombre)

# Función para cargar la lista de rutas de visita en el widget ListBox
def cargar_lista_rutas():
    rutas_listbox.delete(0, tk.END)
    for ruta in rutas:
        rutas_listbox.insert(tk.END, ruta.nombre)

# Función para cargar la lista de ubicaciones en el widget ListBox
def cargar_lista_ubicaciones():
    ubicaciones_listbox.delete(0, tk.END)
    for ubicacion in ubicaciones:
        ubicaciones_listbox.insert(tk.END, ubicacion.nombre)

# Función para cargar la lista de usuarios en el widget ListBox
def cargar_lista_usuarios():
    usuarios_listbox.delete(0, tk.END)
    for usuario in usuarios:
        usuarios_listbox.insert(tk.END, f"{usuario.nombre} {usuario.apellido}")

# Función para cargar la lista de reviews en el widget ListBox
def cargar_lista_reviews():
    reviews_listbox.delete(0, tk.END)
    for review in reviews:
        reviews_listbox.insert(tk.END, f"Evento: {obtener_nombre_evento(review.id_evento)} - "
                                      f"Usuario: {obtener_nombre_usuario(review.id_usuario)}")

# Función para obtener el nombre de un evento por su ID
def obtener_nombre_evento(id_evento):
    for evento in eventos:
        if evento.id == id_evento:
            return evento.nombre
    return ""

# Función para obtener el nombre de un usuario por su ID
def obtener_nombre_usuario(id_usuario):
    for usuario in usuarios:
        if usuario.id == id_usuario:
            return f"{usuario.nombre} {usuario.apellido}"
    return ""

# Función para filtrar los eventos según los criterios seleccionados
def filtrar_eventos():
    nombre = nombre_entry.get()
    genero = genero_entry.get()
    artista = artista_entry.get()
    ubicacion = ubicacion_combobox.get()
    hora_inicio = hora_inicio_entry.get()
    hora_fin = hora_fin_entry.get()

    eventos_filtrados = []

    for evento in eventos:
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

    cargar_lista_eventos_filtrados(eventos_filtrados)

# Función para cargar los eventos filtrados en el widget ListBox
def cargar_lista_eventos_filtrados(eventos_filtrados):
    eventos_listbox.delete(0, tk.END)
    for evento in eventos_filtrados:
        eventos_listbox.insert(tk.END, evento.nombre)

# Función para abrir un archivo JSON con eventos
def abrir_archivo_eventos():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                eventos_data = json.load(file)
            with open('eventos.json', 'w') as file:
                json.dump(eventos_data, file)
            #actualizar_lista_eventos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

# Función para abrir un archivo JSON con rutas de visita
def abrir_archivo_rutas():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                rutas_data = json.load(file)
            with open('rutas.json', 'w') as file:
                json.dump(rutas_data, file)
            #actualizar_lista_rutas()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

# Función para abrir un archivo JSON con ubicaciones
def abrir_archivo_ubicaciones():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                ubicaciones_data = json.load(file)
            with open('ubicaciones.json', 'w') as file:
                json.dump(ubicaciones_data, file)
            #actualizar_lista_ubicaciones()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

# Función para abrir un archivo JSON con usuarios
def abrir_archivo_usuarios():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                usuarios_data = json.load(file)
            with open('usuarios.json', 'w') as file:
                json.dump(usuarios_data, file)
            #actualizar_lista_usuarios()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

# Función para abrir un archivo JSON con reviews
def abrir_archivo_reviews():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                reviews_data = json.load(file)
            with open('reviews.json', 'w') as file:
                json.dump(reviews_data, file)
            #actualizar_lista_reviews()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

# Función para mostrar los detalles de una ubicación seleccionada
def mostrar_detalles_ubicacion(ubicacion):
    messagebox.showinfo("Detalles de la Ubicación",
                        f"Nombre: {ubicacion.nombre}\nDirección: {ubicacion.direccion}\n"
                        f"Coordenadas: {ubicacion.coordenadas}")

# Función para manejar el evento de clic en una ubicación de la lista
def ubicacion_seleccionada(event):
    selected_item = ubicaciones_listbox.get(event.widget.curselection())
    ubicacion = obtener_ubicacion_por_nombre(selected_item)
    if ubicacion:
        mostrar_detalles_ubicacion(ubicacion)

# Función para obtener una ubicación por su nombre
def obtener_ubicacion_por_nombre(nombre):
    for ubicacion in ubicaciones:
        if ubicacion.nombre == nombre:
            return ubicacion
    return None

# Función para cargar los eventos, rutas, ubicaciones, usuarios y reviews y actualizar las listas
def actualizar_listas():
    global eventos, rutas, ubicaciones, usuarios, reviews
    eventos = cargar_eventos()
    rutas = cargar_rutas()
    ubicaciones = cargar_ubicaciones()
    usuarios = cargar_usuarios()
    reviews = cargar_reviews()

    cargar_lista_eventos()
    cargar_lista_rutas()
    cargar_lista_ubicaciones()
    cargar_lista_usuarios()
    cargar_lista_reviews()

# Creación del widget Notebook para las pestañas
notebook = ttk.Notebook(app)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Creación de la pestaña de Eventos
eventos_frame = ttk.Frame(notebook)
notebook.add(eventos_frame, text="Eventos")

# Creación del widget ListBox para mostrar la lista de eventos
eventos_listbox = tk.Listbox(eventos_frame, bg=gris_claro, fg=purpura_oscuro, font=("Arial Black", 12))
eventos_listbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)
eventos_listbox.bind("<<ListboxSelect>>", evento_seleccionado)

# Creación del frame para el panel de búsqueda y filtrado
filtro_frame = ttk.Frame(eventos_frame, padding=10)
filtro_frame.pack(side="left", fill="both", padx=10, pady=10)

# Etiquetas y campos de entrada para los criterios de búsqueda y filtrado
nombre_label = ttk.Label(filtro_frame, text="Nombre:", font=("Arial Black", 12))
nombre_label.pack()
nombre_entry = ttk.Entry(filtro_frame, font=("Arial Black", 12))
nombre_entry.pack(pady=5)

genero_label = ttk.Label(filtro_frame, text="Género:", font=("Arial Black", 12))
genero_label.pack()
genero_entry = ttk.Entry(filtro_frame, font=("Arial Black", 12))
genero_entry.pack(pady=5)

artista_label = ttk.Label(filtro_frame, text="Artista:", font=("Arial Black", 12))
artista_label.pack()
artista_entry = ttk.Entry(filtro_frame, font=("Arial Black", 12))
artista_entry.pack(pady=5)

ubicacion_label = ttk.Label(filtro_frame, text="Ubicación:", font=("Arial Black", 12))
ubicacion_label.pack()
actualizar_listas()
ubicacion_combobox = ttk.Combobox(filtro_frame, values=[ubicaciones.nombre for ubicacion in ubicaciones], 
                                  font=("Arial Black", 12))
ubicacion_combobox.pack(pady=5)

hora_inicio_label = ttk.Label(filtro_frame, text="Hora de Inicio (YYYY-MM-DD HH:MM):", font=("Arial Black", 12))
hora_inicio_label.pack()
hora_inicio_entry = ttk.Entry(filtro_frame, font=("Arial Black", 12))
hora_inicio_entry.pack(pady=5)

hora_fin_label = ttk.Label(filtro_frame, text="Hora de Fin (YYYY-MM-DD HH:MM):", font=("Arial Black", 12))
hora_fin_label.pack()
hora_fin_entry = ttk.Entry(filtro_frame, font=("Arial Black", 12))
hora_fin_entry.pack(pady=5)

# Botón para filtrar los eventos
filtrar_button = ttk.Button(filtro_frame, text="Filtrar", command=filtrar_eventos)
filtrar_button.pack(pady=10)

# Botón para abrir un archivo JSON con eventos
abrir_archivo_eventos_button = ttk.Button(eventos_frame, text="Abrir Archivo de Eventos", 
                                          command=abrir_archivo_eventos)
abrir_archivo_eventos_button.pack(pady=10)

# Creación de la pestaña de Rutas de Visita
rutas_frame = ttk.Frame(notebook)
notebook.add(rutas_frame, text="Rutas de Visita")

# Creación del widget ListBox para mostrar la lista de rutas de visita
rutas_listbox = tk.Listbox(rutas_frame, bg=gris_claro, 
                           fg=purpura_oscuro, font=("Arial Black", 12))
rutas_listbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Botón para abrir un archivo JSON con rutas de visita
abrir_archivo_rutas_button = ttk.Button(rutas_frame, 
                                        text="Abrir Archivo de Rutas", command=abrir_archivo_rutas)
abrir_archivo_rutas_button.pack(pady=10)

# Creación de la pestaña de Ubicaciones
ubicaciones_frame = ttk.Frame(notebook)
notebook.add(ubicaciones_frame, text="Ubicaciones")



# Creación del widget ListBox para mostrar la lista de ubicaciones
ubicaciones_listbox = tk.Listbox(ubicaciones_frame, bg=gris_claro, 
                                 fg=purpura_oscuro, font=("Arial Black", 12))
ubicaciones_listbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)
ubicaciones_listbox.bind("<<ListboxSelect>>", ubicacion_seleccionada)

# Botón para abrir un archivo JSON con ubicaciones
abrir_archivo_ubicaciones_button = ttk.Button(ubicaciones_frame, text="Abrir Archivo de Ubicaciones",
                                              command=abrir_archivo_ubicaciones)
abrir_archivo_ubicaciones_button.pack(pady=10)

# Cargar eventos, rutas, ubicaciones, usuarios y reviews y actualizar las listas
ubicaciones = cargar_ubicaciones()  
actualizar_listas()

# Etiquetas y campos de entrada para las búsquedas y filtrados
nombre_label = ttk.Label(filtro_frame, text="Nombre:", font=("Arial Black", 12))
nombre_label.pack()
nombre_entry = ttk.Entry(filtro_frame, font=("Arial Black", 12))
nombre_entry.pack(pady=5)

genero_label = ttk.Label(filtro_frame, text="Género:", font=("Arial Black", 12))
genero_label.pack()
genero_entry = ttk.Entry(filtro_frame, font=("Arial Black", 12))
genero_entry.pack(pady=5)

artista_label = ttk.Label(filtro_frame, text="Artista:", font=("Arial Black", 12))
artista_label.pack()
artista_entry = ttk.Entry(filtro_frame, font=("Arial Black", 12))
artista_entry.pack(pady=5)

ubicacion_label = ttk.Label(filtro_frame, text="Ubicación:", font=("Arial Black", 12))
ubicacion_label.pack()
ubicacion_combobox = ttk.Combobox(filtro_frame, values=[ubicacion.nombre for ubicacion in ubicaciones], 
                                  font=("Arial Black", 12))
ubicacion_combobox.pack(pady=5)

# Creación de la pestaña de Usuarios
usuarios_frame = ttk.Frame(notebook)
notebook.add(usuarios_frame, text="Usuarios")

# Creación del widget ListBox para mostrar la lista de usuarios
usuarios_listbox = tk.Listbox(usuarios_frame, bg=gris_claro, fg=purpura_oscuro, font=("Arial Black", 12))
usuarios_listbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Botón para abrir un archivo JSON con usuarios
abrir_archivo_usuarios_button = ttk.Button(usuarios_frame, text="Abrir Archivo de Usuarios", command=abrir_archivo_usuarios)
abrir_archivo_usuarios_button.pack(pady=10)

# Creación de la pestaña de Reviews
reviews_frame = ttk.Frame(notebook)
notebook.add(reviews_frame, text="Reviews")

# Creación del widget ListBox para mostrar la lista de reviews
reviews_listbox = tk.Listbox(reviews_frame, bg=gris_claro, fg=purpura_oscuro, font=("Arial Black", 12))
reviews_listbox.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Botón para abrir un archivo JSON con reviews
abrir_archivo_reviews_button = ttk.Button(reviews_frame, text="Abrir Archivo de Reviews", command=abrir_archivo_reviews)
abrir_archivo_reviews_button.pack(pady=10)

# Cargar eventos, rutas, ubicaciones, usuarios y reviews y actualizar las listas
actualizar_listas()

# Ejecución del bucle principal de la aplicación
app.mainloop()

