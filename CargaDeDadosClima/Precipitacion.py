import requests
from datetime import datetime
import pyodbc
# crea una api key en este sitio https://home.openweathermap.org/api_keys
API_KEY = 'Api_key_remplaza_creada'
ciudades_inundadas = [
    'Adamantina', 'Adolfo', 'Águas da Prata', 'Águas de São Pedro', 'Agudos',
    'Aiquara', 'Alambari', 'Alfredo Marcondes', 'Altair',
    'Altinópolis', 'Alto Alegre', 'Alumínio', 'Arujá', 'Aspásia', 'Atibaia',
    'Auriflama', 'Bady Bassitt', 'Bauru', 'Bebedouro',
    'Bento de Abreu', 'Bernardino de Campos', 'Bertioga', 'Bilac', 'Birigui',
    'Biritiba-Mirim', 'Boa Esperança do Sul', 'Bocaina', 'Bofete', 'Botucatu',
    'Bragança Paulista', 'Braúna', 'Brotas', 'Buri', 'Buritama',
    'Cabrália Paulista', 'Caconde', 'Cafelandia', 'Caiabu', 'Caieiras',
    'Caiuá', 'Cajamar', 'Cajati', 'Cajobi', 'Cajuru', 'Campinas',
    'Campo do Tenente', 'Campo Limpo Paulista', 'Capela do Alto', 'Capivari',
    'Caraguatatuba', 'Carapicuíba', 'Casa Branca',
    'Cássia dos Coqueiros', 'Castilho', 'Catanduva', 'Cerqueira César',
    'Cerquilho', 'Charqueada', 'Chavantes', 'Clementina',
    'Colina', 'Colômbia', 'Conchal', 'Conchas', 'Cordeirópolis', 'Corumbataí',
    'Cosmópolis', 'Cotia', 'Cravinhos', 'Cristais Paulista', 'Cruz das Almas',
    'Cubatão', 'Descalvado', 'Diadema', 'Dobrada', 'Dois Córregos',
    'Dolcinópolis', 'Dourado', 'Dracena', 'Duartina', 'Echaporã',
    'Eldorado', 'Elisiário', 'Embu', 'Embu-Guaçu', 'Emilianópolis',
    'Engenheiro Coelho', 'Espírito Santo do Pinhal', 'Estiva Gerbi',
    'Fernandópolis', 'Fernão', 'Ferraz de Vasconcelos', 'Flora Rica',
    'Floreal', 'Florínea', 'Franca', 'Francisco Alves', 'Francisco Morato',
    'Franco da Rocha', 'Gabriel Monteiro', 'Gália', 'Garça', 'Gaviao Peixoto',
    'General Salgado', 'Getulina', 'Glicério', 'Guaira', 'Guaraci',
    'Guarani d\'Oeste', 'Guarujá', 'Guarulhos', 'Hortolândia', 'Iaras',
    'Ibaté', 'Ibiporã', 'Ibirarema', 'Ibitinga', 'Ibiúna', 'Icém', 'Iepê',
    'Igarapava', 'Igaratá', 'Iguape', 'Ilhabela', 'Ilhota', 'Indaiatuba',
    'Indianópolis', 'Indiaporã', 'Inúbia Paulista', 'Itapeva', 'Itapevi',
    'Itapira', 'Itapirapuã Paulista', 'Itápolis', 'Itaquaquecetuba',
    'Itararé', 'Itatiba', 'Itirapina', 'Itobi', 'Itu', 'Jaborandi',
    'Jaboticabal', 'Jacareí', 'Jaguariúna', 'Jales', 'Jambeiro', 'Jandira',
    'Jardinópolis', 'Jarinu', 'Jaú', 'Joaçaba', 'Joanópolis', 'Jundiaí',
    'Juquiá', 'Juquitiba', 'Lagoinha', 'Laranjal Paulista', 'Lavrinhas',
    'Limeira', 'Lindoia', 'Lourdes', 'Lucélia', 'Macaubal', 'Mairinque', 'Mairiporã', 'Manduri',
    'Marabá Paulista', 'Marapoama', 'Marília', 'Matão', 'Mauá', 'Mendonça',
    'Miracatu', 'Mirandópolis', 'Monte Alegre do Sul', 'Monte Alto',
    'Monte Aprazível', 'Monte Mor', 'Morro Agudo', 'Morro do Chapéu',
    'Mundo Novo', 'Murutinga do Sul', 'Natividade da Serra', 'Nazaré Paulista',
    'Neves Paulista', 'Nhandeara', 'Nipoã', 'Nova Aliança', 'Nova Campina',
    'Nova Cantu', 'Nova Europa', 'Nova Granada', 'Nova Iguaçu', 'Nova Odessa',
    'Olímpia', 'Oliveira Barros', 'Osasco', 'Ourinhos', 'Ouro Verde',
    'Pacaembu', 'Palestina', 'Palmital', 'Panorama', 'Paraguaçu Paulista',
    'Paranapanema', 'Parati', 'Pardinho', 'Pariquera-Açu', 'Pedreira',
    'Pedro de Toledo', 'Penápolis', 'Pereira Barreto', 'Pindamonhangaba',
    'Pindorama', 'Pinhalzinho', 'Piracaia', 'Piracicaba', 'Pirassununga',
    'Planalto', 'Poá', 'Poloni', 'Pompéia', 'Pontal', 'Potim', 'Pracinha',
    'Praia Grande', 'Presidente Alves', 'Presidente Epitácio',
    'Presidente Prudente', 'Promissão', 'Quatá', 'Queimadas', 'Quirinópolis',
    'Rafard', 'Rancharia', 'Raposo Tavares', 'Regente Feijó', 'Reginópolis',
    'Ribeirão Bonito', 'Ribeirão Branco', 'Ribeirão Corrente', 'Ribeirão do Sul',
    'Ribeirão Grande', 'Ribeirão Pires', 'Ribeirão Preto', 'Rio Claro',
    'Rio das Pedras', 'Rio Grande da Serra', 'Riolândia', 'Riversul',
    'Rosana', 'Salto', 'Salto Grande', 'Sandovalina', 'Santa Adélia',
    'Santa Albertina', 'Santa Clara do Sul', 'Santa Cruz do Rio Pardo',
    'Santa Fé do Sul', 'Santa Gertrudes', 'Santa Isabel',
    'Santa Rita do Passa Quatro', 'Santa Rosa de Viterbo', 'Santo Anastácio',
    'Santo André', 'Santo Antônio da Alegria', 'Santo Antônio de Posse',
    'Santo Expedito', 'Santos', 'São Bento do Sapucaí', 'São Bernardo do Campo',
    'São Caetano do Sul', 'São Carlos', 'São Francisco', 'São João da Boa Vista',
    'São João de Iracema', 'São Joaquim da Barra', 'São José do Rio Pardo',
    'São José do Rio Preto', 'São Manuel', 'São Paulo', 'São Pedro',
    'São Roque', 'São Sebastião', 'São Simão', 'São Vicente', 'Serrana',
    'Sertãozinho', 'Silvânia', 'Sorocaba', 'Sud Mennucci',
    'Taboão da Serra', 'Tambaú', 'Tanguá', 'Taquaritinga', 'Tatui',
    'Teodoro Sampaio', 'Teófilo Otoni', 'Tietê', 'Torre de Pedra', 'Tremembé',
    'Três Fronteiras', 'Turmalina', 'Ubarana', 'Ubatuba', 'Ubirajara',
    'Utinga', 'Valinhos', 'Vargem Grande do Sul', 'Várzea Paulista', 'Votuporanga',
    'Zacarias'
]

conexion = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=Nome_Servidor;'
        'DATABASE=Nome_Base_dados;'
        'Trusted_Connection=yes;')
cursor = conexion.cursor()

def obtener_datos_meteorologicos(ciudad):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={ciudad},BR&appid={API_KEY}&units=metric'
    response = requests.get(url)
    datos_meteorologicos = response.json()
    
    if response.status_code == 200:
        lluvia_por_dia = {f"{d:02d}": 0 for d in range(1, 32)}
        mes_actual = datetime.now().strftime('%B')
        ano_actual = datetime.now().year
        fecha_actual = datetime.now()

        for item in datos_meteorologicos['list']:
            fecha_hora = item['dt_txt']
            fecha = fecha_hora.split(' ')[0]
            dia = int(fecha.split('-')[2])
            lluvia = item.get('rain', {}).get('3h', 0)

            # Solo considerar los días después de hoy
            if datetime.strptime(fecha, '%Y-%m-%d') > fecha_actual:
                lluvia_por_dia[f"{dia:02d}"] += lluvia

        return lluvia_por_dia, mes_actual, ano_actual
    else:
        print(f"Error en la solicitud para {ciudad}: {datos_meteorologicos.get('message', 'Sin mensaje de error')}")
        return None, None, None

def insertar_o_actualizar_datos(ciudad, lluvia_por_dia, mes, ano):
    consulta_sql_insert = '''
    INSERT INTO Precipitacion (Municipio, Mes, Año, Dia1, Dia2, Dia3, Dia4, Dia5, Dia6, Dia7, Dia8, Dia9, Dia10,
    Dia11, Dia12, Dia13, Dia14, Dia15, Dia16, Dia17, Dia18, Dia19, Dia20, Dia21, Dia22, Dia23, Dia24, Dia25, 
    Dia26, Dia27, Dia28, Dia29, Dia30, Dia31, Total)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    consulta_sql_update = '''
    UPDATE Precipitacion SET 
    Dia1 = ?, Dia2 = ?, Dia3 = ?, Dia4 = ?, Dia5 = ?, Dia6 = ?, Dia7 = ?, Dia8 = ?, Dia9 = ?, Dia10 = ?,
    Dia11 = ?, Dia12 = ?, Dia13 = ?, Dia14 = ?, Dia15 = ?, Dia16 = ?, Dia17 = ?, Dia18 = ?, Dia19 = ?, Dia20 = ?,
    Dia21 = ?, Dia22 = ?, Dia23 = ?, Dia24 = ?, Dia25 = ?, Dia26 = ?, Dia27 = ?, Dia28 = ?, Dia29 = ?, Dia30 = ?,
    Dia31 = ?, Total = ? 
    WHERE Municipio = ? AND Mes = ? AND Año = ?
    '''
    
    valores = [lluvia_por_dia.get(f"{d:02d}", 0) for d in range(1, 32)]
    total_lluvia = sum(valores)

    # Comprobar si ya existen datos para el municipio y el mes
    cursor.execute("SELECT COUNT(*) FROM Precipitacion WHERE Municipio = ? AND Mes = ? AND Año = ?", (ciudad, mes, ano))
    existe = cursor.fetchone()[0] > 0

    if existe:
        # Obtener los datos actuales
        cursor.execute("SELECT Dia1, Dia2, Dia3, Dia4, Dia5, Dia6, Dia7, Dia8, Dia9, Dia10, Dia11, Dia12, Dia13, Dia14, Dia15, Dia16, Dia17, Dia18, Dia19, Dia20, Dia21, Dia22, Dia23, Dia24, Dia25, Dia26, Dia27, Dia28, Dia29, Dia30, Dia31 FROM Precipitacion WHERE Municipio = ? AND Mes = ? AND Año = ?", (ciudad, mes, ano))
        datos_actuales = cursor.fetchone()

        # Actualizar solo los días posteriores
        dia_hoy = datetime.now().day
        print(f"Actualizando datos para {ciudad}...")

        nuevos_valores = []
        for dia in range(1, 32):
            if dia > dia_hoy:
                nuevos_valores.append(valores[dia - 1])  # Actualiza con los nuevos datos
            else:
                nuevos_valores.append(datos_actuales[dia - 1])  # Mantiene los datos existentes

        cursor.execute(consulta_sql_update, *nuevos_valores, total_lluvia, ciudad, mes, ano)
    else:
        # Insertar nuevos datos
        print(f"Insertando datos para {ciudad}...")
        cursor.execute(consulta_sql_insert, ciudad, mes, ano, *valores, total_lluvia)

    conexion.commit()

for ciudad in ciudades_inundadas:
    lluvia_por_dia, mes, ano = obtener_datos_meteorologicos(ciudad)
    if lluvia_por_dia:
        insertar_o_actualizar_datos(ciudad, lluvia_por_dia, mes, ano)

conexion.close()

print("Datos de precipitaciones cargados correctamente en la base de datos.")
