# Primeros pasos con Flask Restful🤖
### 1. Crear un entorno virtual 🐍

```bash
python -m venv venv
# Solo si no funciona el creado
python -m venv venv --without-pip
```

### 2. Activar el entorno virtual ⚡
- En Windows:
    ```bash
        venv\Scripts\activate
    ```
- En gitbash:
    ```
        source venv/Scripts/activate
    ```
- En macOS y Linux:
    ```bash
        source venv/bin/activate
    ```


### 3. Instalar Flask 🛠️

```bash
# Utiliza solo esto si clonaste el proyecto
pip install -r requirements.txt
# Utiliza esto si vas armar desde cero el proyecto
pip install flask Flask-SQLAlchemy Flask-Migrate psycopg2-binary flask-restful
```