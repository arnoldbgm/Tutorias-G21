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

> [!IMPORTANT]
> Antes soliamos crear todas las tablas principales dentro del archivo ahora lo crearemos en el la carpeta ``models`` 📂 si lo hiciste aqui en el ``app`` no te preocupes, lo migraremos a la carpeta ``models``

### 8. Creacion de la base de datos
![image](https://github.com/user-attachments/assets/c012b723-031e-4ab3-a941-af7c64163154)

> [!TIP]
> Si deseas puedes insertar esta data para que practiques tus consultas
```SQL
-- Insertar datos en la tabla Categoria
INSERT INTO Categoria (nombre) VALUES
('Acción'),
('Comedia'),
('Drama'),
('Ciencia Ficción'),
('Terror');

-- Insertar datos en la tabla Pelicula
INSERT INTO Pelicula (titulo, anio, duracion, categoria_id) VALUES
('Mad Max: Fury Road', 2015, 120, 1),
('Deadpool', 2016, 108, 1),
('Superbad', 2007, 113, 2),
('The Hangover', 2009, 100, 2),
('The Shawshank Redemption', 1994, 142, 3),
('Forrest Gump', 1994, 144, 3),
('Inception', 2010, 148, 4),
('Interstellar', 2014, 169, 4),
('The Conjuring', 2013, 112, 5),
('Get Out', 2017, 104, 5);
```

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
---
## Al final nuestro archivo ``app.py`` debe de verse de esta manera

```py
from flask import Flask
from db import db
# Esto me permite controlar las migraciones
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/db_pos'

db.init_app(app)
migrate = Migrate(app, db)

# Este es mi archivo principal, estamos en modo de prueba
if __name__ == '__main__':
   app.run(debug=True)
```

### 10. Crearemos las carpetas `models` y `controllers`📂 

Tu estructura de carpetas se debe de ver de la siguiente forma

```markdown
.
├── controllers
│   └── categoria.py
│   └── peliculas.py
├── models
    └── categoria.py
    └── peliculas.py
``` 
Dentro de nuestro ``models.categorias.py`` debe ir el modelado de nuestra base de datos, lo mismo debes de hacer para ``models.pelicula.py``

```py
# Para crear la tabla de mi base de datos
# Paso 01: Debo de importar
from db import db
from sqlalchemy import Column, Integer, String

# Paso 02: Crear la tabla
class CategoriasModel(db.Model):
   # Colocamos el nombre de la tabla
   __tablename__ = "categorias"

   # Creamos las columnas
   id = Column(Integer, primary_key=True)
   nombre = Column(String)
```

Para poder lograr exportar todos tus modelos, tu debes de crear un archivo dentro  ``models.__init__.py``, esto se hace con el fin de poder exportar toda las clases (tablas) de la carpeta ``models``

```py
from .categoria import CategoriasModel
from .pelicula import PeliculaModel
```

Para que ahora en tu ``app.py`` tu solo coloques 

```py
from flask import Flask
from db import db
from flask_migrate import Migrate
from models import * #Tu con esto puede importar todas la tablas de tu carpeta models
...
```

### 11. Trabajando con los controladores
Los controladores se encargan de manipular toda la parte logica de mi aplicación.

Como creamos un controlador:
```py
from db import db
from models.categoria import  CategoriasModel
from flask_restful import Resource
from flask import request
class CategoriasList(Resource):
   def get(self):
      resultado_consulta = CategoriasModel.query.all()
      print(resultado_consulta)
      return [
         {
            "id": categoria.id,
            "nombre": categoria.nombre,
         } for categoria in resultado_consulta
      ], 200
```
Ahora vamos asociar este controlador a una ruta, nos vamos al archivo ``app.py`` y ahi colocamos lo siguiente

```py
...
from flask_restful import Api
from controllers.categoria import CategoriasList
...
# Crear mi API (Es solo una vez)
api = Api(app)
# Ascociar mis controladores a unas rutas
# api.add_resource( El-nombre-controlador, ruta)
api.add_resource(CategoriasList, "/categorias")

```

Para hacer un POST:

```py
class ProductPost(Resource):
   def post(self):
      data = request.get_json()
      nuevo_categoria = CategoriasModel(**data)
      db.session.add(nuevo_categoria)
      db.session.commit()
      return {
         "message": "Creacion exitosa"
      }, 201
```