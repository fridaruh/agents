
from supabase import create_client
import os
from dotenv import load_dotenv

def get_supabase_client():
    """
    Crea y retorna una conexión al cliente de Supabase
    """
    load_dotenv()  # Carga las variables de entorno del archivo .env
    
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Las credenciales de Supabase no están configuradas")
    
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def get_record_by_address(table_name: str, from_address: str):
    """
    Consulta un registro específico por dirección de contrato en la tabla especificada
    
    Args:
        table_name (str): Nombre de la tabla a consultar
        from_address (str): Dirección de contrato a buscar
    
    Returns:
        dict: Datos del registro encontrado
        None: Si no se encuentra el registro
    """
    try:
        supabase = get_supabase_client()
        
        # Realiza la consulta
        response = (
            supabase.table(table_name)
            .select("*")
            .eq("from_address", from_address)  
            .execute()
        )
        
        # Verifica si se encontraron datos
        if len(response.data) > 0:
            return response.data[0]
        return None
        
    except Exception as e:
        print(f"Error al consultar el registro: {str(e)}")
        raise