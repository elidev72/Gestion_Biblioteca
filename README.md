# Gestión de Biblioteca

### Descripción
Una aplicación para bibliotecarios que permite gestionar libros, clientes, préstamos y devoluciones.

### Diagrama de Clases

### Tecnologías Utilizadas
- Flask v3.1
- SQLAlchemy v2.0.37
- MySQL v8.0.41
- Bulma v1.0.2
- Jinja2 v3.1.5

### Entorno de Desarrollo
- **IDE**: Visual Studio Code
- **Sistema Operativo**: Linux Mint 22
- **Base de Datos**: MySQL (usando DBeaver-ce)
- **Control de Versiones**: Git

### Instrucciones para Ejecutar el Proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/elidev72/Gestion_Biblioteca.git
   cd Gestion_Biblioteca
   ```

2. Crea un entorno virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Windows usa `.venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Importar la base de datos del repositorio.

5. Configurar Variables de Entorno:
    - En la carpeta principal de tu proyecto, crea un archivo llamado `.env`.
    ```
    DB_USER="Tu Usuario"
    DB_PASSWORD="Tu clave"
    DB_HOST=localhost
    DB_NAME=sgb

    SECRET_KEY="Tu Clave Secreta"
   ```

6. Ejecuta la aplicación:
   ```bash
   python3 run.py 
   ```

7. **Credenciales de Prueba**:
   - Para que puedas probar la aplicación con la base de datos de prueba, utiliza las siguientes credenciales:

   | Nombre   | Apellido | Clave         |
   |----------|----------|---------------|
   | Nicole   | Lopez    | 1Mar22        |
   | Juana    | Rojas    | Clave1        |
   | Fernanda | Gomez    | Clave2        |

   - **Instrucciones**:
     - Utiliza estas credenciales para iniciar sesión en la aplicación.
     - Si tienes problemas para acceder, asegúrate de que la base de datos de prueba esté correctamente configurada y en funcionamiento.