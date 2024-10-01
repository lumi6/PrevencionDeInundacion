import overpy
import json

# Crear una instancia de la API de Overpass con un servidor alternativo
api = overpy.Overpass(url="https://overpass-api.de/api/interpreter")

# Consulta para obtener nombres de ríos y lagos en el área de São Paulo
query = """
[out:json][timeout:60]; 
area[name="São Paulo"]->.searchArea; 
(
  way["waterway"="river"](area.searchArea);
  way["natural"="water"](area.searchArea);
);
out body; 
>;
out skel;
"""

try:
    # Ejecutar la consulta
    result = api.query(query)

    # Crear una lista para almacenar los datos en formato deseado
    water_bodies = []

    # Obtener todos los atributos de los ríos y lagos
    for way in result.ways:
        # Crear un diccionario para cada cuerpo de agua
        water_body = {
            "type": "way",
            "id": way.id,
            "nodes": [node.id for node in way.nodes],  # Obtener IDs de los nodos
            "tags": way.tags  # Obtener todos los tags
        }
        water_bodies.append(water_body)

    # Imprimir los resultados en formato JSON
    print(json.dumps(water_bodies, indent=2, ensure_ascii=False))

except overpy.exception.OverpassUnknownHTTPStatusCode as e:
    print(f"Error durante la consulta a la API de Overpass: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
