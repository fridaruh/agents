# Importa las funciones
from conexion_datos import get_record_by_address

#solicitar el contact_address
from_address = input("Ingrese la wallet: ")

# Ejemplo de uso
try:
    # Reemplaza 'nombre_tabla' con el nombre de tu tabla real
    # y '1' con el ID que quieras consultar
    resultado = get_record_by_address('tornado', from_address)
    if resultado:
        print("Registro encontrado:", resultado)
    else:
        print("No se encontró el registro")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")