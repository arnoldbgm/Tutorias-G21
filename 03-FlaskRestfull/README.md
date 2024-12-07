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


### 4. Crear un archivo `app.py` 📄
Debemos de partir creando un archivo llamado `app.py` ahi es donde es iniciara nuestro servidor

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a mi primera app de Flask 😎'

if __name__ == '__main__':
    app.run(debug=True)

```

### 5. Ejecutar la aplicación ▶️

```bash
# Puedo levantar mi servidor con esto
python app.py
# Tambien lo puedo levantar de esta forma
flask run

```

### 6. Configuracion de SQLAlchemy
```
pip install -U Flask-SQLAlchemy
```
> [!TIP]
> Creamos el archivo `db.py` para centralizar la instancia de `SQLAlchemy` y facilitar su importación y reutilización en diferentes partes del proyecto Flask. Esto asegura una estructura limpia y modular, permitiendo que otros módulos (como modelos o rutas) accedan a la base de datos sin redundancia en el código.

```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

Ahora llamaremos a nuestro archivo `db.py` en nuestro `app.py`


```py
from flask import Flask
from db import db

# Debo ejecutarlo (instanciarlo)
app = Flask(__name__)

# Ejecutamos SQLAlchemy 
db.init_app(app)

if __name__ == '__main__':
   app.run(debug=True)
```

### 7. Conectar a una base de datos con Flask-SQLAlchemy 🔗

> [!IMPORTANT]
> Antes de poder conectarnos a la bd, debemos de tener Flask Migrate instalado y configurado

```
pip install Flask-Migrate psycopg2-binary
```

```python
from flask import Flask
from db import db
from sqlalchemy import Column, Integer, String
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:my_password@localhost:5432/punto_de_venta'

db.init_app(app)
migrate = Migrate(app, db)

class Movies(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    director = Column(String(200))
    year = Column(Integer)
    length_minutes = Column(Integer)

if __name__ == '__main__':
    app.run(debug=True)

```

### 8. Creacion de la base de datos
![Bd](https://github.com/user-attachments/assets/4d7782ba-62e0-4148-88c9-7674e17e3d41)

### 9. Ejecutar la migración 🚀

- **Ejecutar la instancia de las migraciones**:
    
    ```bash
    flask db init
    
    ```
    
- **Crear la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db migrate -m "0001-Creacion de BD"
    
    ```
    
- **Aplicar la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db upgrade
    ```
    
### 10. Crearemos las carpetas `models` y `controllers`📂 

Tu estructura de carpetas se debe de ver de la siguiente forma

```markdown
.
├── controllers
│   └── products.py
├── models
    └── products.py
``` 