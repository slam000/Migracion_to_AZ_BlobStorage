# Migración a Azure Blob Storage

Este proyecto proporciona un script en Python diseñado para automatizar la migración de archivos a Azure Blob Storage, incluyendo la asignación de etiquetas a los archivos subidos. Es ideal para proyectos que requieren una organización eficiente y una recuperación fácil de archivos en el almacenamiento en la nube.

## Características

- Carga de archivos JSON y CSV desde un directorio local.
- Conversión de archivos JSON y CSV a estructuras de datos de Python para su manejo.
- Carga segura de claves de cuentas de almacenamiento de Azure desde un archivo JSON.
- Subida de archivos a Azure Blob Storage con asignación de etiquetas para una organización eficiente.

## Requisitos

Para ejecutar este script, necesitarás:

- Python 3.6 o superior.
- Bibliotecas de Python: `azure-storage-blob`, `json`, `csv`, `os`.
- Credenciales de Azure Blob Storage (nombre de la cuenta y claves de acceso).

## Instalación

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

## Configuración

```markdown
# Migración a Azure Blob Storage

Este proyecto proporciona un script en Python diseñado para automatizar la migración de archivos a Azure Blob Storage, incluyendo la asignación de etiquetas a los archivos subidos. Es ideal para proyectos que requieren una organización eficiente y una recuperación fácil de archivos en el almacenamiento en la nube.

## Características

- Carga de archivos JSON y CSV desde un directorio local.
- Conversión de archivos JSON y CSV a estructuras de datos de Python para su manejo.
- Carga segura de claves de cuentas de almacenamiento de Azure desde un archivo JSON.
- Subida de archivos a Azure Blob Storage con asignación de etiquetas para una organización eficiente.

## Requisitos

Para ejecutar este script, necesitarás:

- Python 3.6 o superior.
- Bibliotecas de Python: `azure-storage-blob`, `json`, `csv`, `os`.
- Credenciales de Azure Blob Storage (nombre de la cuenta y claves de acceso).

## Instalación

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## Configuración

Antes de ejecutar el script, asegúrate de tener los siguientes archivos en el directorio `docs/`:

- `TagsByStorage.json`: Mapeo de tipos de documentos a sus respectivos almacenamientos en Azure Blob Storage.
- `indice_migracion_junio_2024.csv`: Índice de los archivos a migrar, incluyendo el camino local, el nombre del contenedor y el tipo de documento.
- `StorageAccountsAndKeys.json`: Claves de acceso para las cuentas de almacenamiento de Azure utilizadas.

## Uso

Para ejecutar el script de migración, simplemente ejecuta:

```bash
python app.py
```

El script procesará cada registro en el archivo CSV, subirá el archivo correspondiente a Azure Blob Storage y le asignará la etiqueta adecuada.

## Contribuir

Las contribuciones son bienvenidas. Si tienes una sugerencia para mejorar este proyecto, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo `LICENSE` para más detalles.
```