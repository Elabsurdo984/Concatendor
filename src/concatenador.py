import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
import csv
import os
from datetime import datetime

class FileConcatenatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Concatenador de Archivos")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")
        
        # Variables
        self.selected_files = []
        self.output_directory = os.path.expanduser("~\\Documents")
        self.custom_filename = tk.StringVar(value="archivo_concatenado")
        
        self.create_gui()
        
    def create_gui(self):
        # Estilo
        style = ttk.Style()
        style.configure("TButton", padding=5, font=('Helvetica', 10))
        style.configure("TLabel", background="#f0f0f0", font=('Helvetica', 10))
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text="🔄 Super Concatenador de Archivos", 
            font=('Helvetica', 16, 'bold')
        )
        title_label.pack(pady=10)
        
        # Frame para opciones de archivo
        file_frame = ttk.LabelFrame(main_frame, text="Opciones de Archivo", padding="5")
        file_frame.pack(fill=tk.X, pady=5)
        
        # Botones de selección
        ttk.Button(
            file_frame,
            text="📂 Seleccionar Archivos",
            command=self.select_files
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            file_frame,
            text="📁 Cambiar Directorio de Salida",
            command=self.change_output_directory
        ).pack(side=tk.LEFT, padx=5)
        
        # Frame para nombre personalizado
        name_frame = ttk.LabelFrame(main_frame, text="Nombre del Archivo", padding="5")
        name_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(name_frame, text="Nombre:").pack(side=tk.LEFT, padx=5)
        ttk.Entry(
            name_frame,
            textvariable=self.custom_filename
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # Lista de archivos seleccionados
        files_frame = ttk.LabelFrame(main_frame, text="Archivos Seleccionados", padding="5")
        files_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.files_text = ScrolledText(files_frame, height=10)
        self.files_text.pack(fill=tk.BOTH, expand=True)
        
        # Opciones de concatenación
        options_frame = ttk.LabelFrame(main_frame, text="Opciones de Concatenación", padding="5")
        options_frame.pack(fill=tk.X, pady=5)
        
        self.add_header = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            options_frame,
            text="Incluir encabezados en archivos CSV",
            variable=self.add_header
        ).pack(anchor=tk.W)
        
        self.add_filename = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            options_frame,
            text="Agregar nombre de archivo como comentario",
            variable=self.add_filename
        ).pack(anchor=tk.W)
        
        # Nuevo checkbox para quitar la primera línea
        self.remove_first_line = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            options_frame,
            text="Quitar primera línea de cada archivo (excepto el primero si se incluye encabezado)",
            variable=self.remove_first_line
        ).pack(anchor=tk.W)
        
        # Botón de concatenación
        ttk.Button(
            main_frame,
            text="🔄 Concatenar Archivos",
            command=self.concatenate_files,
            style="TButton"
        ).pack(pady=10)
        
        # Barra de estado
        self.status_label = ttk.Label(
            main_frame,
            text="Listo para concatenar archivos",
            font=('Helvetica', 9)
        )
        self.status_label.pack(pady=5)
        
    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Selecciona archivos para concatenar",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Archivos CSV", "*.csv"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if files:
            self.selected_files = files
            self.update_files_list()
            
    def update_files_list(self):
        self.files_text.delete(1.0, tk.END)
        for i, file in enumerate(self.selected_files, 1):
            self.files_text.insert(tk.END, f"{i}. {os.path.basename(file)}\n")
            
    def change_output_directory(self):
        directory = filedialog.askdirectory(
            title="Selecciona el directorio de salida"
        )
        if directory:
            self.output_directory = directory
            self.status_label.config(
                text=f"Directorio de salida: {os.path.basename(directory)}"
            )
            
    def concatenate_files(self):
        if not self.selected_files:
            messagebox.showwarning(
                "Advertencia",
                "Por favor selecciona archivos para concatenar"
            )
            return
            
        try:
            # Determinar el tipo de archivo por la extensión del primer archivo
            extension = os.path.splitext(self.selected_files[0])[1].lower()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"{self.custom_filename.get()}_{timestamp}{extension}"
            output_path = os.path.join(self.output_directory, output_filename)
            
            if extension == '.csv':
                self.concatenate_csv_files(output_path)
            else:
                self.concatenate_text_files(output_path)
                
            messagebox.showinfo(
                "Éxito",
                f"Archivos concatenados exitosamente en:\n{output_path}"
            )
            
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Error al concatenar archivos:\n{str(e)}"
            )
            
    def concatenate_csv_files(self, output_path):
        with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            
            for i, file in enumerate(self.selected_files):
                with open(file, 'r', encoding='utf-8') as infile:
                    reader = csv.reader(infile)
                    
                    if self.add_filename.get():
                        writer.writerow([f"# Archivo: {os.path.basename(file)}"])
                    
                    # Determinar si debemos incluir la primera línea de este archivo
                    include_first_line = (i == 0 and self.add_header.get()) or not self.remove_first_line.get()
                    
                    if include_first_line:
                        # Leer todas las filas incluyendo la primera
                        for row in reader:
                            writer.writerow(row)
                    else:
                        # Saltar la primera línea
                        next(reader, None)  # El None es para evitar errores si el archivo está vacío
                        for row in reader:
                            writer.writerow(row)
                            
    def concatenate_text_files(self, output_path):
        with open(output_path, 'w', encoding='utf-8') as outfile:
            for i, file in enumerate(self.selected_files):
                if self.add_filename.get():
                    outfile.write(f"\n# Archivo: {os.path.basename(file)}\n")
                
                with open(file, 'r', encoding='utf-8') as infile:
                    # Determinar si debemos incluir la primera línea de este archivo
                    include_first_line = (i == 0 and self.add_header.get()) or not self.remove_first_line.get()
                    
                    if include_first_line:
                        # Leer todo el contenido normalmente
                        outfile.write(infile.read())
                    else:
                        # Saltar la primera línea
                        lines = infile.readlines()
                        if lines:  # Verificar que el archivo no esté vacío
                            outfile.write(''.join(lines[1:]))  # Unir las líneas desde la segunda hasta el final
                
                outfile.write('\n')

if __name__ == "__main__":
    root = tk.Tk()
    app = FileConcatenatorApp(root)
    root.mainloop()