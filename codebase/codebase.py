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
style.configure("TLabel", background="#2F242C", foreground="#E5E5E5", font=("Open Sans", 12))
style.configure("TButton", background="#E6D884", foreground="#2F242C", font=("Roboto", 12))

# Creación del widget ListBox para mostrar la lista de eventos
eventos_listbox = tk.Listbox(root, bg="#E5E5E5", fg="#2F242C", font=("Open Sans", 12))
eventos_listbox.pack(padx=10, pady=10)
eventos_listbox.bind("<<ListboxSelect>>", evento_seleccionado)

# Botón para abrir un archivo JSON con eventos
abrir_archivo_button = ttk.Button(root, text="Abrir Archivo", command=abrir_archivo)
abrir_archivo_button.pack(pady=10)

# Cargar eventos iniciales
eventos = cargar_eventos()
cargar_lista_eventos()

# Ejecución del bucle principal de la aplicación

root.mainloop()
