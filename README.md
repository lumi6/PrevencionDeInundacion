# Prevención de Inundaciones en São Paulo

Este proyecto tiene como objetivo recolectar datos climáticos de diferentes sitios web, incluyendo coordenadas de ríos, para predecir y prevenir inundaciones en los municipios del estado de São Paulo.

## Descripción del Proyecto

El proyecto se divide en varios pasos que incluyen la creación de una base de datos, la recolección y carga de datos climáticos, y la obtención de coordenadas de ríos mediante diferentes APIs. A continuación se describen los pasos necesarios para ejecutar el proyecto.

## 1. Creación de la Base de Datos

El primer paso es crear la base de datos en **SQL Server** (puedes usar otro gestor de bases de datos si lo prefieres). 

- **Archivo a ejecutar**: `DadosClima.sql`
  - Este script se encargará de generar las tablas necesarias para almacenar los datos climáticos.

## 2. Configuración y Carga de Datos Climáticos

Una vez creada la base de datos, necesitamos cargar los datos del clima utilizando tres archivos Python que se encuentran en la carpeta `cargadedadosclima`. Antes de ejecutar estos archivos, debes modificar algunas variables importantes:

### a. Modificar la API Key

Debes obtener una API key de [OpenWeatherMap](https://openweathermap.org/api) para acceder a los datos climáticos.

- Modifica la variable `API_KEY` en cada uno de los archivos `.py` de la carpeta `cargadedadosclima`:
  python
  API_KEY = 'tu_api_key'
### b. Configurar la Conexión a la Base de Datos
Asegúrate de modificar la configuración de la conexión a la base de datos según el gestor de bases de datos que estés utilizando (SQL Server, MySQL, etc.). La conexión debe ser personalizada en cada uno de los archivos .py.

### c. Ejecutar los Programas
Una vez hechas estas modificaciones, ejecuta los tres archivos Python de la carpeta cargadedadosclima para cargar los datos climáticos en tu base de datos.

### 3. Carga de Coordenadas de Lagos y Ríos
Además de los datos climáticos, este proyecto también recolecta coordenadas de lagos y ríos para la prevención de inundaciones.

### a. Registro en OpenStreetMap
Debes registrarte en OpenStreetMap para visualizar el mapa y acceder a las coordenadas.

### b. Consultas en Overpass Turbo
Utiliza la plataforma Overpass Turbo para realizar consultas en formato JSON que te permitirán obtener las coordenadas precisas de ríos y lagos.

Este paso es aún experimental, por lo que cualquier contribución es bienvenida para mejorar la recolección y uso de estos datos.

Contribuciones

Este proyecto está en desarrollo, por lo que cualquier sugerencia o modificación será de gran ayuda. Si tienes ideas para mejorar el código o agregar nuevas funcionalidades, no dudes en realizar un pull request o abrir un issue.

