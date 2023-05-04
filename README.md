# Quick-Image-Table-Api
API para Quick Image Table v2 - En Django REST Framework

## Deployed API
https://quickimage.pythonanywhere.com/api/

## Detalles y como ejecutar en local
En el repositorio se dispone de la versión "entre casa".  
Base de datos SQLite, superusuario "Carlos", contraseña "12345".  

Pasos para probar en local.

 ```sh
git clone https://github.com/carlosmperilla/Quick-Image-Table-Api.git
python -m venv qit-env
quit-env\Scripts\activate
pip install -r requirements.txt
cd quickimagetable_data
python -m manage runserver 0.0.0.0:8000
```

## Endpoint principales y documentación
La API es navegable "Browsable" para los amigos.  
Pero es necesario loggearse primero para poder ver la documentación.  
Recordando, para la API local es "Carlos: 12345", aunque puede cambiarlo a su superusuario de preferencia.  
Para la API lanzada, debe usar su usuario registrado en Quick Image Table v2, disponible en mis repositorios.  


### Cuenta con las siguientes documentaciones:
- Propia del API navegable, cada pagina posee la información de uso y los paneles de uso, muy propio de Django REST Framework.
- Swagger: http://127.0.0.1:8000/api/swagger/
- ReDoc: http://127.0.0.1:8000/api/redoc/

### Endpoints principales
- Stocks: http://127.0.0.1:8000/api/stocks/
- Products: http://127.0.0.1:8000/api/products/
