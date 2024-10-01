import requests
import pandas as pd
import pyodbc
from datetime import datetime

# crea una api key en este sitio https://home.openweathermap.org/api_keys
API_KEY = 'Api_key_remplaza_creada'
MUNICIPIO = 'Campinas'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={MUNICIPIO}&appid={API_KEY}&units=metric"

# Función para obtener los datos meteorológicos
def obtener_datos_meteorologicos():
    response = requests.get(URL)
    data = response.json()

    if response.status_code != 200:
        print("Error al obtener datos:", data.get("message", ""))
        return None
    
    # Crear una lista para almacenar los datos
    dias = []
    
    # Recorrer los datos de pronóstico
    for item in data['list']:
        fecha = datetime.fromtimestamp(item['dt'])
        dia = fecha.day
        mes = fecha.strftime("%B")
        año = fecha.year
        precipitacion = item.get('rain', {}).get('1h', 0)  # Obtener precipitación en la última hora

        # Agregar datos al diccionario
        dias.append({
            'Municipio': MUNICIPIO,
            'Mes': mes,
            'Año': año,
            'Dia': dia,
            'Precipitacion': precipitacion
        })

    return dias

# Conexión a SQL Server
def insertar_datos_a_sql(df):
    # Configura la conexión a tu base de datos SQL Server
    connection_string = (
       'DRIVER={SQL Server};'
        'SERVER=Nome_Servidor;'
        'DATABASE=Nome_Base_dados;'
        'Trusted_Connection=yes;'
    )
    
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        
        # Verificar si ya existe un registro para el mes y año actual
        for index, row in df.iterrows():
            cursor.execute("""
                SELECT COUNT(*) FROM Precipitacion 
                WHERE Municipio = ? AND Mes = ? AND Año = ?
            """, row['Municipio'], row['Mes'], row['Año'])
            exists = cursor.fetchone()[0]
            
            if exists == 0:
                # Si no existe, crear una nueva fila para ese mes y año
                insert_query = f"""
                    INSERT INTO Precipitacion (Municipio, Mes, Año, Dia1, Dia2, Dia3, Dia4, Dia5, Dia6, Dia7,
                        Dia8, Dia9, Dia10, Dia11, Dia12, Dia13, Dia14, Dia15, Dia16, Dia17, Dia18, Dia19,
                        Dia20, Dia21, Dia22, Dia23, Dia24, Dia25, Dia26, Dia27, Dia28, Dia29, Dia30, Dia31, Total)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?)
                """
                # Crear una lista de precipitaciones inicializadas en 0
                dias_preci = [0] * 31  # 31 días
                # Asignar la precipitación al día correspondiente
                dias_preci[row['Dia'] - 1] = row['Precipitacion']
                
                # Calcular el total de precipitaciones
                total_precipitacion = sum(dias_preci)

                # Insertar en la base de datos
                cursor.execute(insert_query, row['Municipio'], row['Mes'], row['Año'], *dias_preci, total_precipitacion)
            else:
                # Si existe, actualizar la fila correspondiente
                update_query = f"""
                    UPDATE Precipitacion 
                    SET Dia{row['Dia']} = Dia{row['Dia']} + ?, Total = Total + ? 
                    WHERE Municipio = ? AND Mes = ? AND Año = ?
                """
                cursor.execute(update_query, row['Precipitacion'], row['Precipitacion'], row['Municipio'], row['Mes'], row['Año'])
        
        conn.commit()  # Confirmar los cambios en la base de datos

# Obtener datos de Campinas
datos_campinas = obtener_datos_meteorologicos()

# Crear un DataFrame para los resultados
if datos_campinas:
    df = pd.DataFrame(datos_campinas)

    # Agrupar por municipio, mes, año y día y sumar precipitaciones
    df_grouped = df.groupby(['Municipio', 'Mes', 'Año', 'Dia']).sum().reset_index()
    
    # Insertar datos en la base de datos
    insertar_datos_a_sql(df_grouped)
    print("Datos insertados en la base de datos.")
else:
    print("No se pudieron obtener los datos.")
