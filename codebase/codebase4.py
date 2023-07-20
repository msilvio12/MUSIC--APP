import json
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage 
import tkintermapview
from PIL import Image, ImageTk



# Colores personalizados
purpura_oscuro = "#2F242C"
gris_claro = "#E5E5E5"
amarillo = "#E6D884"
verde_claro = "#A1A892"


# CONFIGURACION DE VENTANA 
app = tk.Tk()
app.geometry("600x400")
app.configure(bg=purpura_oscuro)  # Color de fondo principal







# CLASE EVENTO
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

# CLASE RUTA DE VISITA
class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def __str__(self):
        return f"Ruta de Visita: {self.nombre}"

# CLASE UBICACION
class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

    def __str__(self):
        return f"Ubicación: {self.nombre}"

# CLASE USUARIO
class Usuario:
    def __init__(self, id, nombre, apellido, historial_eventos):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = historial_eventos

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}"

# CLASE REVIEW
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

# FUNCION PARA CARGAR LOS EVENTOS DESDE UN ARCHIVO JSON
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

# FUNCION PARA CARGAR LAS RUTAS DE VISITA DESDE UN ARCHIVO JSON
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

# FUNCION PARA CARGAR LAS UBICACIONES DESDE UN ARCHIVO JSON
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

# FUNCION PARA CARGAR LOS USUARIOS DESDE UN ARCHIVO JSON
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

# FUNCION PARA CARGAR LAS REVIEWS DESDE UN ARCHIVO JSON
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

# FUNCION PARA MOSTRAR LOS DETALLES DE UN EVENTO SELECCIONADO
def mostrar_detalles_evento(evento):
    messagebox.showinfo("Detalles del Evento",
                        f"Nombre: {evento.nombre}\nArtista: {evento.artista}\nGénero: {evento.genero}\n"
                        f"Ubicación: {evento.id_ubicacion}\nHora de Inicio: {evento.hora_inicio}\n"
                        f"Hora de Fin: {evento.hora_fin}\nDescripción: {evento.descripcion}")

# FUNCION PARA MANEJAR EL EVENTO DE CLIC EN UN EVENTO DE LA LISTA
def evento_seleccionado(event):
    selected_item = eventos_listbox.get(event.widget.curselection())
    evento = obtener_evento_por_nombre(selected_item) # revisar funcion, tiene un error
    if evento:
        mostrar_detalles_evento(evento)

# FUNCION PARA OBTENER UN EVENTO POR SU NOMBRE
def obtener_evento_por_nombre(nombre):
    for evento in eventos:
        if evento.nombre == nombre:
            return evento
    return None

# FUNCION PARA CARGAR LA LISTA DE EVENTOS EN EL LISTBOX
def cargar_lista_eventos():
    eventos_listbox.delete(0, tk.END)
    for evento in eventos:
        eventos_listbox.insert(tk.END, evento.nombre)

# FUNCION PARA CARGAR LA LISTA DE RUTAS DE VISITA EN EL LISTBOX
def cargar_lista_rutas():
    rutas_listbox.delete(0, tk.END)
    for ruta in rutas:
        rutas_listbox.insert(tk.END, ruta.nombre)

# FUNCION PARA CARGAR LA LISTA DE UBICACIONES EN LISTBOX
def cargar_lista_ubicaciones():
    ubicaciones_listbox.delete(0, tk.END)
    for ubicacion in ubicaciones:
        ubicaciones_listbox.insert(tk.END, ubicacion.nombre)

# FUNCION PARA CARGAR UNA LISTA DE USUARIOS EN LISTBOX
def cargar_lista_usuarios():
    usuarios_listbox.delete(0, tk.END)
    for usuario in usuarios:
        usuarios_listbox.insert(tk.END, f"{usuario.nombre} {usuario.apellido}")

# FUNCION PARA CARGAR LA LISTA DE REVIEWS EN LISTBOX
def cargar_lista_reviews():
    reviews_listbox.delete(0, tk.END)
    for review in reviews:
        reviews_listbox.insert(tk.END, f"Evento: {obtener_nombre_evento(review.id_evento)} - "
                                      f"Usuario: {obtener_nombre_usuario(review.id_usuario)}")

# FUNCION PARA OBTENER EL NOMBRE DE UN EVENTO POR SU ID
def obtener_nombre_evento(id_evento):
    for evento in eventos:
        if evento.id == id_evento:
            return evento.nombre
    return ""

# FUNCION PARA OBTENER EL NOMBRE DE UN USUARIO POR SU ID 
def obtener_nombre_usuario(id_usuario):
    for usuario in usuarios:
        if usuario.id == id_usuario:
            return f"{usuario.nombre} {usuario.apellido}"
    return ""

# FUNCION PARA FILTRAR LOS EVENTOS SEGUN LO SELECCIONADO
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

# FUNCION PAR CARGAR LOS EVENTOS FILTRADOS EN EL WIDGET LISTBOX
def cargar_lista_eventos_filtrados(eventos_filtrados):
    eventos_listbox.delete(0, tk.END)
    for evento in eventos_filtrados:
        eventos_listbox.insert(tk.END, evento.nombre)

# FUNCION PARA ABRIR UN ARCHIVO JSON CON EVENTOS 
def abrir_archivo_eventos():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                eventos_data = json.load(file)
            with open('eventos.json', 'w') as file:
                json.dump(eventos_data, file)
            actualizar_listas()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

# FUNCION PARA ABRIR UN ARCHIVO JSON CON RUTAS DE VISITAS
def abrir_archivo_rutas():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                rutas_data = json.load(file)
            with open('rutas.json', 'w') as file:
                json.dump(rutas_data, file)
            actualizar_listas()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

# FUNCION PARA ABRIR UN ARCHIVO JSON CON UBICACIONES
def abrir_archivo_ubicaciones():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                ubicaciones_data = json.load(file)
            with open('ubicaciones.json', 'w') as file:
                json.dump(ubicaciones_data, file)
            actualizar_listas()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

# FUNCION PARA ABRIR UN ARCHIVO JSON CON USUARIOS
def abrir_archivo_usuarios():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                usuarios_data = json.load(file)
            with open('usuarios.json', 'w') as file:
                json.dump(usuarios_data, file)
            actualizar_listas()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

# FUNCION PARA ABRIR UN ARCHIVO JSON CON REVIEWS
def abrir_archivo_reviews():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                reviews_data = json.load(file)
            with open('reviews.json', 'w') as file:
                json.dump(reviews_data, file)
            actualizar_listas()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

#FUNCION PARA ACTUALIZAR LAS LISTAS DE EVENTOS, RUTAS, ETC
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

# CARGAR LOS DATOS INICIALES
eventos = cargar_eventos()
rutas = cargar_rutas()
ubicaciones = cargar_ubicaciones()
usuarios = cargar_usuarios()
reviews = cargar_reviews()

# CONFIGURACION DE LA PANTALLA PRINCIPAL
#app.title("Aplicación de Eventos")
#app.resizable(True, True)

# CONFIGURACION DE PANTALLA DETALLES DEL EVENTO
detalles_evento_screen = tk.Toplevel(app)
detalles_evento_screen.title("Detalles del Evento")
detalles_evento_screen.geometry("600x400")
detalles_evento_screen.withdraw()

#CONFIGURACION DE PANTALLA PRINCIPAL
botones_frame = tk.Frame(app, bg=purpura_oscuro)
botones_frame.pack(pady=20)
background_image = tk.PhotoImage(file="assets/5571.png")
background_image = background_image.subsample(26) #SUBSAMPLE: TAMAÑO DE LA IMAGEN


# CREAR EL WIDGET DEL MAPA
map_widget = tkintermapview.TkinterMapView(app, width=600, height=400, corner_radius=20) #borde de esquinas del mapa

# COORDENADAS PARA EL WIDGET
map_widget.place(relx=1.0, rely=0.6, anchor=tk.CENTER) #posición del mapa

# LOCALIZACION DEL MAPA
map_widget.set_position(-24.7829, -65.4232)  # Salta, Argentina
map_widget.set_zoom(14)


# CONFIGURACION DEL WIDGET LABEL PARA LA IMAGEN DE FONDO
background_label = tk.Label(app, image=background_image, bg=purpura_oscuro)
background_label.place(x=-456, y=80, relwidth=1, relheight=1)


eventos_button = tk.Button(botones_frame, text="Índice de Eventos", font=("Arial Black", 16),
                           bg=amarillo, command=cargar_lista_eventos)
eventos_button.grid(row=0, column=0, padx=10)

busqueda_button = tk.Button(botones_frame, text="Búsqueda y Filtrado de Eventos",font=("Arial Black", 16), 
                            bg=amarillo, command=filtrar_eventos)
busqueda_button.grid(row=0, column=1, padx=10)

historial_button = tk.Button(botones_frame, text="Historial de Eventos", font=("Arial Black", 16),
                             bg=amarillo, command=cargar_lista_eventos)
historial_button.grid(row=0, column=2, padx=10)

# CONFIGURACION DE LA PANTALLA DE DETALLES DE EVENTO
detalles_evento_label = tk.Label(detalles_evento_screen, text="Detalles del Evento", 
                                 font=("Arial black", 16),
                                bg=purpura_oscuro, fg=gris_claro)
detalles_evento_label.pack(pady=20)

mapa_label = tk.Label(detalles_evento_screen, text="Mapa", font=("Arial black", 12), 
                      bg=purpura_oscuro, fg=gris_claro)
mapa_label.pack()

reviews_label = tk.Label(detalles_evento_screen, text="Reviews", font=("Arial black", 12), 
                         bg=purpura_oscuro, fg=gris_claro)
reviews_label.pack()

# CONFIGURACION DEL WIDGET LISTBOX PARA MOSTRAR LISTA DE EVENTOS
eventos_listbox = tk.Listbox(app, width=60, height=10)
eventos_listbox.pack(pady=20)
eventos_listbox.bind('<<ListboxSelect>>', evento_seleccionado)

# CONFIGURACION DEL WIDGET ENTRY Y BUTTON PARA FILTRAR EVENTOS 
filtro_frame = tk.Frame(app, bg=amarillo)
filtro_frame.pack(pady=10)

nombre_label = tk.Label(filtro_frame, text="Nombre:", font=("Arial Black", 16),
                        bg=amarillo, fg="black")
nombre_label.grid(row=0, column=0, padx=10)

nombre_entry = tk.Entry(filtro_frame)
nombre_entry.grid(row=0, column=1, padx=10)

genero_label = tk.Label(filtro_frame, text="Género:", font=("Arial Black", 16), 
                        bg=amarillo, fg="black")
genero_label.grid(row=0, column=2, padx=10)

genero_entry = tk.Entry(filtro_frame)
genero_entry.grid(row=0, column=3, padx=10)

artista_label = tk.Label(filtro_frame, text="Artista:", font=("Arial Black", 16),
                         bg=amarillo, fg="black")
artista_label.grid(row=1, column=0, padx=10)

artista_entry = tk.Entry(filtro_frame)
artista_entry.grid(row=1, column=1, padx=10)

ubicacion_label = tk.Label(filtro_frame, text="Ubicación:", font=("Arial Black", 16), 
                           bg=amarillo, fg="black")
ubicacion_label.grid(row=1, column=2, padx=10)

ubicacion_combobox = ttk.Combobox(filtro_frame, 
                                  values=[ubicacion.nombre for ubicacion in ubicaciones])
ubicacion_combobox.grid(row=1, column=3, padx=10)

hora_inicio_label = tk.Label(filtro_frame, text="Hora de Inicio:", font=("Arial Black", 16), 
                             bg=amarillo, fg="black")
hora_inicio_label.grid(row=2, column=0, padx=10)

hora_inicio_entry = tk.Entry(filtro_frame)
hora_inicio_entry.grid(row=2, column=1, padx=10)

hora_fin_label = tk.Label(filtro_frame, text="Hora de Fin:", font=("Arial Black", 16),
                          bg=amarillo, fg="black")
hora_fin_label.grid(row=2, column=2, padx=10)

hora_fin_entry = tk.Entry(filtro_frame)
hora_fin_entry.grid(row=2, column=3, padx=10)

filtrar_button = tk.Button(app, text="Filtrar", font=("Arial Black", 12),
                           bg=verde_claro, command=filtrar_eventos)
filtrar_button.pack(pady=10)

# CONFIGURACION DEL WIDGET LISTBOX PARA MOSTRAR RUTAS DE VISITA
rutas_listbox = tk.Listbox(app, width=60, height=10)
rutas_listbox.pack(pady=20)

# CONFIGURACION DEL WIDGET PARA MOSTRAR LISTA DE UBICACIONES
ubicaciones_listbox = tk.Listbox(app, width=60, height=10)
ubicaciones_listbox.pack(pady=20)

# CONFIGURACION DEL WIDGET LISTBOX PARA MOSTRAR LISTA DE USUARIOS
usuarios_listbox = tk.Listbox(app, width=60, height=10)
usuarios_listbox.pack(pady=20)

# CONFIGURACION DEL WIDGET LISTBOX PARA MOSTRAR LISTA DE REVIEWS
reviews_listbox = tk.Listbox(app, width=60, height=10)
reviews_listbox.pack(pady=20)

# CONFIGURACION DEL MENU 
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

# MEMU ARCHIVO
archivo_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
                    

# CONFIGURACION MENU INTERNO
archivo_menu.configure(font=("Arial Black", 10), fg="black", bg="#E6D884")
archivo_menu.add_command(label="Abrir Eventos", command=abrir_archivo_eventos)
archivo_menu.add_command(label="Abrir Rutas", command=abrir_archivo_rutas)
archivo_menu.add_command(label="Abrir Ubicaciones", command=abrir_archivo_ubicaciones)
archivo_menu.add_command(label="Abrir Usuarios", command=abrir_archivo_usuarios)
archivo_menu.add_command(label="Abrir Reviews", command=abrir_archivo_reviews)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=app.quit)


# ACTUALIZAR LAS LISTAS AL INICIAR LA APLICACION 
actualizar_listas()


app.mainloop()


 
 
 






 


        
        
        
        