import json
import csv
import os
from azure.storage.blob import BlobServiceClient

# Cargar documento JSON de docs/ y convertirlo en un diccionario
def cargar_json(file_path):
    with open(file_path) as f:
        return json.load(f)

# Cargar documento CSV de docs/ y convertirlo en una lista de diccionarios
def cargar_csv(file_path, delimiter=';'):
    with open(file_path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter=delimiter))

# Cargar JSON Storage Account Keys de docs/ y convertirlo en un diccionario
def cargar_storage_account_keys(file_path):
    with open(file_path) as f:
        return json.load(f)

# Obtener la cadena de conexión de la cuenta de almacenamiento
def obtener_cadena_conexion(storage_account_name, storage_account_keys):
    for account in storage_account_keys:
        if account['Name'] == storage_account_name:
            return account['StringConnection']
    return None

# Subir archivo a Blob Storage y agregar etiquetas
def subir_y_etiquetar_archivo(blob_client, local_path, tags):
    with open(local_path, 'rb') as data:
        blob_client.upload_blob(data, overwrite=True)
    blob_client.set_blob_tags(tags)

def main():
    """
    Función principal del script de migración legal.

    Carga los documentos necesarios, procesa cada registro del CSV y sube el archivo correspondiente
    al almacenamiento adecuado. También agrega una etiqueta al archivo subido.

    Args:
        None

    Returns:
        None
    """
    # Cargar documentos
    tags_by_storage = cargar_json('docs/TagsByStorage.json')
    registros_csv = cargar_csv('docs/indice_migracion_junio_2024.csv', delimiter=';')
    storage_account_keys = cargar_storage_account_keys('docs/StorageAccountsAndKeys.json')

    # Crear un diccionario para buscar el almacenamiento por tipo de documento
    tag_storage_dict = {item['documentType']: item['storage'] for item in tags_by_storage}
    
    # Crear un diccionario para buscar las conexiones rápidamente
    connection_dict = {account['Name']: account['StringConnection'] for account in storage_account_keys}

    # lineasProcesadas = 0
    lineasProcesadas = 0
    lineasTotales = len(registros_csv)
    print(f"Procesando {lineasTotales} registros...")
    
    # Procesar cada registro del CSV y subir el archivo correspondiente
    for registro in registros_csv:
        local_path = registro['Path']
        container_name = registro['ContainerName']
        document_type = registro['TagDocumentType']
        document_name = os.path.basename(local_path)
        lineasProcesadas += 1
        
        print(f"\033[42m\033[30mProcesando {lineasProcesadas}/{lineasTotales} - {local_path}\033[0m")
        
        # Determinar el almacenamiento correcto según el tipo de documento
        storage_account_name = tag_storage_dict.get(document_type)
        
        if not storage_account_name:
            print(f"\033[43m\033[30mNo se encontró almacenamiento para el tipo de documento: {document_type}\033[0m")
            continue
        
        # Obtener el cliente del blob
        connection_string = obtener_cadena_conexion(storage_account_name, storage_account_keys)
        if not connection_string:
            print(f"\033[43m\033[30mNo se encontró la cadena de conexión para la cuenta de almacenamiento: {storage_account_name}\033[0m")
            continue
        
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=document_name)
        
        print(f"\033[94mSubiendo {local_path} a {container_name}/{document_name} en {storage_account_name}\033[0m")
        
        # Subir el archivo y agregar la etiqueta
        subir_y_etiquetar_archivo(blob_client, local_path, {'documentType': document_type})
        
        print(f"Etiqueta {{'documentType': '{document_type}'}} añadida a {container_name}/{document_name}")
    print("Proceso completado.")

if __name__ == '__main__':
    main()
