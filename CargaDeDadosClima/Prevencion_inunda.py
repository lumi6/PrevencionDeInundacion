import requests
import pyodbc
from datetime import datetime, timedelta

# crea una api key en este sitio https://home.openweathermap.org/api_keys
API_KEY = 'Api_key_remplaza_creada'
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

# Función de predicción de riesgo de inundación
def predecir_riesgo_inundacion(temperatura, umidade, vento):
    if temperatura > 30 and umidade > 80 and vento > 10:
        return 'Alto', 'Condiciones severas: calor extremo, alta humedad y vientos fuertes.'
    elif 20 < temperatura <= 30 and 60 <= umidade <= 80 and 5 <= vento <= 10:
        return 'Moderado', 'Posible riesgo moderado de inundación con lluvias.'
    else:
        return 'Bajo', 'Bajo riesgo de inundación.'

# Función para obtener predicciones meteorológicas
def obtener_datos_meteorologicos(municipio):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={municipio},BR&appid={API_KEY}&units=metric"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        temperatura = datos['main']['temp']
        umidade = datos['main']['humidity']
        vento = datos['wind']['speed']
        return {
            'municipio': municipio,
            'temperatura': temperatura,
            'umidade': umidade,
            'vento': vento
        }
    else:
        print(f"No se pudo obtener datos para {municipio}: {respuesta.status_code}")
        return None

# Función para insertar o actualizar datos en la tabla Previsao_Inundacao
def insertar_o_actualizar_prediccion(dados, fecha_prediccion):
    conexion = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=Nome_Servidor;'
        'DATABASE=Nome_Base_dados;'
        'Trusted_Connection=yes;')
    cursor = conexion.cursor()

    for dado in dados:
        riesgo_inundacao, observacion = predecir_riesgo_inundacion(dado['temperatura'], dado['umidade'], dado['vento'])
        
        # Convertir la fecha a cadena para evitar problemas con pyodbc
        fecha_prediccion_str = fecha_prediccion.strftime('%Y-%m-%d')
        
        # Verificar si ya existe un registro para el municipio y la fecha
        cursor.execute("""
            SELECT COUNT(*) FROM Previsao_Inundacao
            WHERE Municipio = ? AND CAST(data_previsao AS DATE) = ?
        """, (dado['municipio'], fecha_prediccion_str))
        existe = cursor.fetchone()[0]

        if existe:
            # Actualizar el registro para días futuros
            cursor.execute("""
                UPDATE Previsao_Inundacao
                SET risco_inundacao = ?, observacao = ?
                WHERE Municipio = ? AND CAST(data_previsao AS DATE) = ?
            """, (riesgo_inundacao, observacion, dado['municipio'], fecha_prediccion_str))
            print(f"Actualizado: {dado['municipio']} para la fecha {fecha_prediccion_str}")
        else:
            # Insertar nuevo registro si no existe
            cursor.execute("""
                INSERT INTO Previsao_Inundacao (Municipio, risco_inundacao, data_previsao, observacao)
                VALUES (?, ?, ?, ?)
            """, (dado['municipio'], riesgo_inundacao, fecha_prediccion_str, observacion))
            print(f"Insertado: {dado['municipio']} para la fecha {fecha_prediccion_str}")

    conexion.commit()
    cursor.close()
    conexion.close()

# Función principal para obtener datos y predecir para los próximos 5 días
def predecir_y_guardar():
    hoy = datetime.now()
    dados_a_guardar = []

    # Obtener datos para hoy
    for municipio in municipios:
        datos_meteorologicos = obtener_datos_meteorologicos(municipio)
        if datos_meteorologicos:
            dados_a_guardar.append(datos_meteorologicos)
    
    # Guardar predicción de hoy
    insertar_o_actualizar_prediccion(dados_a_guardar, hoy)
    
    # Actualizar predicciones para los próximos 5 días
    for i in range(1, 6):
        fecha_futura = hoy + timedelta(days=i)
        insertar_o_actualizar_prediccion(dados_a_guardar, fecha_futura)

# Llamar a la función para predecir y guardar
predecir_y_guardar()
