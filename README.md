# Buy n Large Store API

Este proyecto consiste en una API para una tienda en línea con un asistente virtual integrado usando LangChain y Groq. El proyecto está dividido en dos partes: backend (Django) y frontend (React + TypeScript).


https://github.com/user-attachments/assets/31273c74-9e2a-4218-9be1-ee6adaded358


## Requisitos Previos

- Python 3.10 o superior
- Node.js 18 o superior
- PostgreSQL 14 o superior
- Una cuenta en Groq para el API key

## Estructura del Proyecto

```
buynlarge/
├── backend/         # Proyecto Django
│   ├── store_api/   # Configuración principal
│   ├── authentication/
│   ├── products/
│   ├── orders/
│   ├── customers/
│   └── llm_graph/   # Asistente virtual
└── frontend/        # Aplicación React
```

## Configuración del Backend

1. Crear y activar un entorno virtual:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
   - Crear un archivo `.env` en la raíz del proyecto:
```env
DEBUG=True
SECRET_KEY=your-secret-key
GROQ_API_KEY=your-groq-api-key

# Database
DB_NAME=storedb
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

4. Crear la base de datos en PostgreSQL:
```bash
createdb storedb
```

5. Ejecutar migraciones:
```bash
python manage.py migrate
```

6. Poblar la base de datos con datos de ejemplo:
```bash
python manage.py seed_database
```

7. Crear un superusuario (opcional):
```bash
python manage.py createsuperuser
```

8. Iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

El backend estará disponible en `http://localhost:8000`

## Configuración del Frontend

1. Navegar al directorio frontend:
```bash
cd frontend
```

2. Instalar dependencias:
```bash
npm install
```

3. Iniciar el servidor de desarrollo:
```bash
npm run dev
```

El frontend estará disponible en `http://localhost:5173`

## Endpoints Principales

### Autenticación
- POST `/api/auth/register/` - Registro de usuarios
- POST `/api/auth/login/` - Inicio de sesión


### Asistente Virtual
- POST `/api/llm/ask/` - Endpoint para hacer preguntas al asistente

## Características Principales

- Asistente virtual con LangChain y Groq
- Interfaz de chat para comunicarse con el asistente
- Sistema de gestión de productos y órdenes
- Base de datos PostgreSQL

## Desarrollo

### Comandos Útiles

Backend:
```bash
# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ejecutar tests
python manage.py test
```

Frontend:
```bash
# Ejecutar tests
npm test

# Construir para producción
npm run build
```

## Solución de Problemas Comunes

1. Error de CORS:
   - Asegúrate de que el backend esté corriendo en `http://localhost:8000`
   - Verifica que las configuraciones de CORS en `settings.py` sean correctas

2. Error de conexión a la base de datos:
   - Verifica que PostgreSQL esté corriendo
   - Confirma las credenciales en el archivo `.env`

3. Error con el API de Groq:
   - Verifica que tu API key sea válida
   - Asegúrate de que esté correctamente configurada en el archivo `.env`

## Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles. 
