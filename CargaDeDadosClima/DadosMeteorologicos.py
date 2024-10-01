import requests
import pyodbc
from datetime import datetime, timedelta
# crea una api key en este sitio https://home.openweathermap.org/api_keys
API_KEY = 'Api_key_remplaza_creada'
# Lista de municipios de São Paulo
municipios = [
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
    'Zacarias']

# Función para obtener datos meteorológicos
def obtener_datos_meteorologicos(municipio):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={municipio},BR&appid={API_KEY}&units=metric"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        forecast_data = []
        
        for item in datos['list']:
            temperatura = item['main']['temp']
            umidade = item['main']['humidity']
            vento = item['wind']['speed']
            fecha_hora = datetime.fromtimestamp(item['dt'])  # Convertir a datetime
            
            # Solo guardar datos de los próximos 5 días
            if fecha_hora >= datetime.now():
                forecast_data.append({
                    'municipio': municipio,
                    'temperatura': temperatura,
                    'umidade': umidade,
                    'vento': vento,
                    'data_hora': fecha_hora
                })
        
        return forecast_data
    else:
        print(f"No se pudo obtener datos para {municipio}: {respuesta.status_code}")
        return None

# Función para insertar o actualizar datos en la base de datos SQL Server
def insertar_o_actualizar_dados(datos):
    # Conectar a la base de datos
    conexion = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=Nome_Servidor;'
        'DATABASE=Nome_Base_dados;'
        'Trusted_Connection=yes;')
    cursor = conexion.cursor()
    
    for dado in datos:
        # Verificar si ya existe un registro para el municipio y la fecha y hora
        cursor.execute("""
            SELECT COUNT(*) FROM Dados_Meteorologicos
            WHERE Municipio = ? AND data_hora = ?
        """, (dado['municipio'], dado['data_hora']))
        existe = cursor.fetchone()[0]

        if existe:
            # Actualizar el registro existente
            cursor.execute("""
                UPDATE Dados_Meteorologicos
                SET temperatura = ?, umidade = ?, vento = ?, data_hora = ?
                WHERE Municipio = ? AND data_hora = ?
            """, (dado['temperatura'], dado['umidade'], dado['vento'], dado['data_hora'], dado['municipio'], dado['data_hora']))
            print(f"Actualizado: {dado['municipio']} para la fecha y hora {dado['data_hora']}")
        else:
            # Insertar nuevo registro
            cursor.execute("""
                INSERT INTO Dados_Meteorologicos (Municipio, temperatura, umidade, vento, data_hora)
                VALUES (?, ?, ?, ?, ?)
            """, (dado['municipio'], dado['temperatura'], dado['umidade'], dado['vento'], dado['data_hora']))
            print(f"Insertado: {dado['municipio']} para la fecha y hora {dado['data_hora']}")
    
    # Guardar cambios y cerrar la conexión
    conexion.commit()
    cursor.close()
    conexion.close()

# Obtener datos para cada municipio y almacenarlos
dados_a_guardar = []
for municipio in municipios:
    dados_meteorologicos = obtener_datos_meteorologicos(municipio)
    if dados_meteorologicos:
        dados_a_guardar.extend(dados_meteorologicos)  # Usar extend para agregar múltiples entradas

# Llamar a la función para insertar o actualizar datos en la base de datos
insertar_o_actualizar_dados(dados_a_guardar)
