# Super Concatenador de Archivos

## Descripción
El Super Concatenador de Archivos es una herramienta de escritorio con interfaz gráfica que permite unir múltiples archivos CSV o TXT en un solo archivo. Está diseñada para facilitar la consolidación de datos de manera rápida y sencilla, especialmente útil para usuarios que trabajan con conjuntos de datos divididos en múltiples archivos.

## Características
- **Interfaz gráfica intuitiva**: Fácil de usar para usuarios con cualquier nivel de experiencia técnica.
- **Soporte para archivos CSV y TXT**: Concatena archivos del mismo formato manteniendo su estructura.
- **Opciones de personalización**:
  - Incluir o excluir encabezados en archivos CSV
  - Agregar comentarios con el nombre del archivo original
  - Quitar la primera línea de cada archivo (útil para archivos con encabezados repetidos)
- **Directorio de salida configurable**: Elige dónde guardar el archivo concatenado.
- **Nombre personalizable**: Define el nombre base del archivo de salida.
- **Marca de tiempo automática**: Cada archivo generado incluye fecha y hora para evitar sobrescrituras.

## Requisitos
- Python 3.13 o superior
- Tkinter (incluido en la mayoría de las instalaciones estándar de Python)

## Instalación

### Opción 1: Ejecutar desde el código fuente
1. Asegúrate de tener Python instalado en tu sistema
2. Clona o descarga este repositorio
3. Navega hasta el directorio del proyecto
4. Ejecuta el script principal:
   ```
   python src/concatenador.py
   ```

### Opción 2: Crear un ejecutable (Windows)
1. Instala PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Crea el ejecutable:
   ```
   pyinstaller --onefile --windowed src/concatenador.py
   ```
3. El ejecutable se generará en la carpeta `dist`

### Opcion 3: Instalarlo manual

1. Ve a la derecha de este repositorio
2. Dirijite a la carpeta Releases
3. Descarga el ejecutable (Solo windows)

## Uso

1. **Inicia** la aplicación.
2. **Selecciona los archivos** que deseas concatenar usando el botón "Seleccionar Archivos".
3. **Configura las opciones**:
   - **Directorio de salida**: Cambia dónde se guardará el archivo concatenado.
   - **Nombre del archivo**: Personaliza el nombre base del archivo.
   - **Opciones de concatenación**:
     - **Incluir encabezados**: Si marcas esta opción, se mantienen los encabezados en archivos CSV.
     - **Agregar nombre de archivo**: Inserta un comentario con el nombre del archivo original.
     - **Quitar primera línea**: Elimina la primera línea de cada archivo (excepto del primero si se incluyen encabezados).
4. **Haz clic** en "Concatenar Archivos".
5. **Revisa** el mensaje de confirmación con la ubicación del archivo generado.

## Casos de uso comunes

### Unir archivos CSV con encabezados
Ideal para cuando tienes varios archivos CSV con la misma estructura de columnas:
- Marca "Incluir encabezados" si quieres mantener el encabezado del primer archivo.
- Marca "Quitar primera línea" para eliminar los encabezados redundantes en archivos posteriores.

### Unir archivos de texto
Para combinar archivos de texto como logs, informes o cualquier dato textual:
- Usa la opción "Agregar nombre de archivo" para identificar de qué archivo proviene cada sección.
- La opción "Quitar primera línea" también funciona con archivos TXT.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor:
1. Haz un fork del repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit a tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia
Este proyecto está licenciado bajo GPL v3.0.
