from conexion_datos import get_record_by_address
from agente_v1 import analyze_wallet, fecha_generacion

def main():
    # Solicitar el contact_address
    from_address = input("Ingrese la wallet: ")

    try:
        ###### Tornado Cash ######
        resultado = get_record_by_address('tornado', from_address)
        
        if resultado:
            print("Procesando wallet...")
            # Analizar la wallet usando la función de abejas.py
            analisis = analyze_wallet(from_address)
            print("\nAnálisis de la wallet:")
            print("Generated at: "+ fecha_generacion + "\n" + analisis)
            
            
        else:
            print("No se encontró el registro en la tabla tornado cash")
            
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    main()
