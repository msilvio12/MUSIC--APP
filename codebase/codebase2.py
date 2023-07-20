import json
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import customtkinter 
from tkinter import PhotoImage


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x400")

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

# Función para cargar los eventos y actualizar la lista
def actualizar_lista_eventos():
    eventos = cargar_eventos()
    cargar_lista_eventos()

# Función para abrir un archivo JSON con eventos
def abrir_archivo():
    filepath = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if filepath:
        try:
            with open(filepath, 'r') as file:
                eventos_data = json.load(file)
            with open('eventos.json', 'w') as file:
                json.dump(eventos_data, file)
            actualizar_lista_eventos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")

# Creación de la ventana principal
root = tk.Tk()
root.title("App de Eventos Musicales")
root.configure(bg="#2F242C")  # Color de fondo principal

# Estilo para los widgets
style = ttk.Style()
style.configure("TLabel", background="#2F242C", foreground="#E5E5E5", font=("Arial Black", 12))
style.configure("TButton", background="#E6D884", foreground="#2F242C", font=("Arial Black", 12))

# Creación del widget ListBox para mostrar la lista de eventos
eventos_listbox = tk.Listbox(root, bg="#E5E5E5", fg="#2F242C", font=("Open Sans", 12))
eventos_listbox.pack(padx=10, pady=10)
eventos_listbox.bind("<<ListboxSelect>>", evento_seleccionado)

# Frame para el panel de búsqueda y filtrado
filtro_frame = ttk.Frame(root, padding=10)
filtro_frame.pack(fill="both", expand=True)

# Etiquetas y campos de entrada para búsqueda y filtrado
nombre_label = ttk.Label(filtro_frame, text="Nombre:")
nombre_label.grid(row=0, column=0, sticky="e")
nombre_entry = ttk.Entry(filtro_frame, width=60)
nombre_entry.grid(row=0, column=1, padx=5)

genero_label = ttk.Label(filtro_frame, text="Género:")
genero_label.grid(row=0, column=2, sticky="e")
genero_entry = ttk.Entry(filtro_frame, width=60)
genero_entry.grid(row=0, column=3, padx=5)

artista_label = ttk.Label(filtro_frame, text="Artista:")
artista_label.grid(row=1, column=0, sticky="e")
artista_entry = ttk.Entry(filtro_frame, width=60)
artista_entry.grid(row=1, column=1, padx=5)

ubicacion_label = ttk.Label(filtro_frame, text="Ubicación:")
ubicacion_label.grid(row=1, column=2, sticky="e")
ubicacion_combobox = ttk.Combobox(filtro_frame, values=["Ubicación 1", "Ubicación 2", "Ubicación 3"], width=57)
ubicacion_combobox.grid(row=1, column=3, padx=5)

hora_inicio_label = ttk.Label(filtro_frame, text="Hora de Inicio:")
hora_inicio_label.grid(row=2, column=0, sticky="e")
hora_inicio_entry = ttk.Entry(filtro_frame, width=60)
hora_inicio_entry.grid(row=2, column=1, padx=5)

hora_fin_label = ttk.Label(filtro_frame, text="Hora de Fin:")
hora_fin_label.grid(row=2, column=2, sticky="e")
hora_fin_entry = ttk.Entry(filtro_frame, width=60)
hora_fin_entry.grid(row=2, column=3, padx=5)

filtrar_button = ttk.Button(filtro_frame, text="Filtrar", command=filtrar_eventos)
filtrar_button.grid(row=3, columnspan=4, pady=20)

# Botón para abrir un archivo JSON con eventos
abrir_archivo_button = ttk.Button(root, text="Abrir Archivo", command=abrir_archivo)
abrir_archivo_button.pack(pady=10)

# Cargar eventos iniciales
eventos = cargar_eventos()
cargar_lista_eventos()

# Configurar el fondo de la aplicación con una imagen
image = PhotoImage(file="path/to/image.png")
background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Ejecución del bucle principal de la aplicación
root.mainloop()


