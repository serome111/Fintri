# FastAPI con PostgreSQL

Este proyecto es una API desarrollada con [FastAPI](https://fastapi.tiangolo.com/) que interactúa con una base de datos PostgreSQL. Utiliza [SQLAlchemy](https://www.sqlalchemy.org/) como ORM y [Pydantic](https://pydantic-docs.helpmanual.io/) para la validación de datos. El proyecto está configurado para ejecutarse en contenedores Docker, facilitando su despliegue y ejecución.

## Requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [uv en docker](https://ryxcommar.com/2024/02/15/how-to-cut-your-python-docker-builds-in-half-with-uv/)
## Estructura del Proyecto

my_fastapi_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── transaccion.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── transaccion.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── transaccion.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── transaccion.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_transaccion.py
│   ├── utils/
│       ├── __init__.py
│       ├── helper.py
├── .env
├── requirements.txt
├── alembic/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
└── alembic.ini


Detalle de la Estructura
1. app/: Carpeta principal del código de la aplicación.
2. app/main.py: Punto de entrada de la aplicación FastAPI.
3. app/core/: Configuraciones principales y archivos de inicialización de la aplicación.
 * config.py: Configuraciones de la aplicación, como variables de entorno.
4. app/db/: Archivos relacionados con la base de datos.
 * database.py: Configuración y conexión a la base de datos.
5. app/models/: Modelos de datos SQLAlchemy o Pydantic.
 * transaccion.py: Definiciones de los modelos de la tabla Transacciones.
6. app/schemas/: Esquemas de Pydantic para validación y serialización de datos.
 * transaccion.py: Esquemas relacionados con la tabla Transacciones.
7. app/crud/: Funciones de CRUD (Create, Read, Update, Delete).
 * transaccion.py: Funciones CRUD para la tabla Transacciones.
8. app/routers/: Routers de FastAPI que contienen los endpoints de la aplicación.
 * transaccion.py: Endpoints relacionados con Transacciones.
9. app/tests/: Archivos de pruebas.
 * test_transaccion.py: Pruebas unitarias y funcionales para Transacciones.
10.app/utils/: Utilidades y funciones helper.
 * helper.py: Funciones auxiliares que pueden ser utilizadas en diferentes partes de la aplicación.
11. .env: Archivo de variables de entorno.
12. requirements.txt: Archivo de dependencias del proyecto.
13. alembic/ y alembic.ini: Archivos de configuración y scripts de migraciones de base de datos con Alembic.
