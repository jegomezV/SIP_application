# Sistema de Gestión Escolar

[![Banner application](https://i.imgur.com/WvFuAkt.png)](https://i.imgur.com/WvFuAkt.png)

Este proyecto consiste en el desarrollo de una aplicación web para gestionar operaciones clave de una institución educativa, como el registro de estudiantes, salones, materias y el seguimiento de la asistencia.

### Requisitos Previos

Asegúrate de cumplir con los siguientes requisitos antes de intentar ejecutar el proyecto:
- Python (versión 3.7 o superior) instalado en tu sistema.
- PostgreSQL instalado y configurado (opcional, dependiendo de la configuración del proyecto).
- Docker instalado (opcional, si prefieres ejecutar el proyecto en un contenedor).

### Instalación de Dependencias

1. Accede al directorio del proyecto y crea un entorno virtual. Luego, instala las dependencias necesarias:
    ```bash
    cd Web2py_application
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Clona el repositorio:
    ```bash
    git clone https://github.com/jegomezV/Web2py_application.git
    ```

### Configuración de la Base de Datos

Si el proyecto utiliza una base de datos PostgreSQL y necesitas configurarla, asegúrate de crear la base de datos y configurar las credenciales adecuadas en el archivo de configuración.

### Ejecución del Proyecto

1. Ejecuta las migraciones (si es necesario):
    ```bash
    alembic upgrade head
    ```

2. Inicia la aplicación:
    ```bash
    python web2py.py
    ```

Esto iniciará el servidor web local y podrás acceder a la aplicación desde tu navegador web en la dirección [http://localhost:8000](http://localhost:8000).


## Autor

- [jegomezV](https://github.com/jegomezV)

- [linkedin](https://www.linkedin.com/in/jegomez-v/)
