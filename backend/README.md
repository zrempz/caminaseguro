# Backend – API RESTful (Django + MongoDB)

Este directorio contiene la API RESTful del proyecto CaminaSeguro, construida con Django y conectada a MongoDB a través de MongoEngine.

## Requisitos

- Python 3.10+

# Instalación

1. **Crear y activar entorno virtual**

   ```bash
   # Crear el entorno
   python -m venv venv

   # Activar en Linux/macOS
   source venv/bin/activate

   # Activar en Windows
   .\venv\Scripts\activate
   ```

2. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**
   - Copiar `.env.example` a `.env`
   - Completar la cadena de conexión a MongoDB y otros valores sensibles.

## Ejecución en desarrollo

Para iniciar el servidor de desarrollo de la API:

```bash
python manage.py runserver
```

Una vez ejecutado, la API quedará disponible en: `http://127.0.0.1:8000`

## Endpoints clave

| Método |         Ruta          |                         Descripción |
| :----- | :-------------------: | ----------------------------------: |
| `POST` | `/api/auth/registro/` |         Registro de nuevos usuarios |
| `POST` |  `/api/auth/login/`   | Inicio de sesión y obtención de JWT |
| `GET`  | `/api/auth/usuario/`  |       Datos del usuario autenticado |

Todos los endpoints devuelven respuestas en formato **JSON** y cumplen con los estándares **RESTful**.
