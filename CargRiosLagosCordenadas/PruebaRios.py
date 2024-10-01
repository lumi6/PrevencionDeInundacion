import overpy

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
"""

try:
    # Ejecutar la consulta
    result = api.query(query)

    # Obtener solo los nombres de los ríos y lagos
    names = [way.tags.get("name", "Sin nombre") for way in result.ways]

    # Eliminar duplicados y nombres vacíos
    names = list(set(filter(lambda name: name != "Sin nombre", names)))

    # Imprimir los nombres
    for name in names:
        print(name)

except overpy.exception.OverpassUnknownHTTPStatusCode as e:
    print(f"Error durante la consulta a la API de Overpass: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
