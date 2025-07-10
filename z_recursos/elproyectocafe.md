¡Excelente iniciativa! Construir un proyecto CRUD en Django es una de las mejores formas de aprender y consolidar los fundamentos del framework. A continuación, te presento una guía completa y detallada, paso a paso, para crear la aplicación que solicitas, incluyendo las mejoras, explicaciones y la presentación elegante que pides.

---

### **Resumen del Proyecto**

Crearemos una aplicación web para gestionar un catálogo de cafés. Esta aplicación permitirá realizar las operaciones **CRUD** (Crear, Leer, Actualizar y Borrar) sobre los productos de café. La vista principal mostrará los cafés en tarjetas, similar a la imagen proporcionada, y tendremos formularios para añadir, editar y eliminar productos.

### **Conceptos Clave a Entender**

*   **Django:** Un framework de alto nivel para Python que promueve el desarrollo rápido y un diseño limpio y pragmático.
*   **MVT (Modelo-Vista-Plantilla):** Es el patrón de arquitectura que usa Django.
    *   **Modelo (Model):** La capa de datos. Define la estructura de tu información (tablas en la base de datos).
    *   **Vista (View):** La capa de lógica. Recibe peticiones web y devuelve respuestas. Interactúa con el Modelo para obtener datos.
    *   **Plantilla (Template):** La capa de presentación. Es el archivo HTML que se muestra al usuario, con datos insertados por la Vista.
*   **Entorno Virtual:** Un directorio aislado que contiene una instalación de Python y paquetes específicos para un proyecto, evitando conflictos entre dependencias de diferentes proyectos.
*   **ORM (Object-Relational Mapper):** Herramienta de Django que permite interactuar con la base de datos usando código Python (clases y objetos) en lugar de escribir SQL directamente.

---

### **Paso 1: Preparación del Entorno Virtual**

Es una buena práctica fundamental trabajar siempre dentro de un entorno virtual.

1.  **Abre tu terminal** o línea de comandos.
2.  Navega a la carpeta donde quieres guardar tu proyecto (ej. `Documentos/Proyectos/`).
3.  Crea el entorno virtual. Lo llamaremos `venv`.
    ```bash
    python -m venv venv
    ```
4.  Activa el entorno virtual. El comando varía según tu sistema operativo:
    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```
    Verás `(venv)` al principio de la línea de tu terminal, indicando que está activo.

**Resumen del Punto:** Hemos creado un espacio de trabajo aislado para nuestro proyecto, asegurando que las librerías que instalemos no afecten a otros proyectos.

---

### **Paso 2: Instalación de Django**

Con el entorno virtual activo, instala Django usando `pip`, el gestor de paquetes de Python.

```bash
pip install django
```

---

### **Paso 3: Creación del Proyecto y la Aplicación**

1.  **Crear el proyecto Django:** Un proyecto es el contenedor de toda la configuración y las aplicaciones. Usaremos el nombre `backend_pcafe`. El `.` al final evita crear un subdirectorio extra.
    ```bash
    django-admin startproject backend_pcafe .
    ```
2.  **Crear la aplicación:** Una aplicación es un módulo que realiza una función específica (en nuestro caso, gestionar el café).
    ```bash
    python manage.py startapp frontend_appcafe
    ```

**Resumen del Punto:** Hemos establecido la estructura base de Django: un "proyecto" general que contiene una "aplicación" específica para nuestra lógica de café.

---

### **Paso 4: Mejorando el Modelo y Creando la Base de Datos**

Abriremos el archivo `frontend_appcafe/models.py` y definiremos nuestro modelo `Cafe`. Haremos algunas mejoras al modelo que propusiste para que sea más robusto y semánticamente correcto.

**Mejoras al modelo:**

*   `precio`: Usaremos `DecimalField` en lugar de `FloatField` para trabajar con dinero, ya que evita problemas de precisión con puntos flotantes.
*   `cantidad`: La renombraremos a `stock` para que sea más descriptivo y usaremos `PositiveIntegerField` para asegurar que no pueda ser un número negativo.
*   `imagen_red`: Usaremos `URLField` que es específico para guardar URLs.
*   `__str__`: Añadiremos este método para que los objetos `Cafe` se muestren de forma legible en el panel de administración de Django.

**Código para `frontend_appcafe/models.py`:**

```python
from django.db import models

class Cafe(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Mejor para precios
    stock = models.PositiveIntegerField() # Mejor para cantidades/inventario
    imagen_url = models.URLField(max_length=2048) # Mejor para URLs de imágenes

    def __str__(self):
        return self.nombre
```

**Crear las Migraciones:** Ahora, le decimos a Django que prepare los cambios para la base de datos.

```bash
python manage.py makemigrations
python manage.py migrate
```

**Resumen del Punto:** Hemos definido la estructura de nuestros datos en Python. Django ha traducido esa definición a un formato que la base de datos entiende (migraciones) y ha creado las tablas correspondientes.

---

### **Paso 5: Configuraciones Clave (`settings.py` y `urls.py`)**

1.  **Registrar la aplicación:** En el archivo `backend_pcafe/settings.py`, Django necesita saber que nuestra aplicación `frontend_appcafe` existe. Añádela a la lista `INSTALLED_APPS`.

    ```python
    # backend_pcafe/settings.py
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'frontend_appcafe',  # Añadir esta línea
    ]
    ```

2.  **Configurar las URLs del proyecto:** Edita `backend_pcafe/urls.py` para que las peticiones a la URL principal (`/`) sean gestionadas por nuestra aplicación.

    ```python
    # backend_pcafe/urls.py
    
    from django.contrib import admin
    from django.urls import path, include # Asegúrate de importar include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('frontend_appcafe.urls')), # Añadir esta línea
    ]
    ```

**Resumen del Punto:** Hemos conectado nuestra aplicación al proyecto principal, diciéndole a Django que la considere parte del sistema y que dirija todo el tráfico web hacia ella para que sea procesado.

---

### **Paso 6: URLs de la Aplicación y Lógica de Vistas**

1.  **Crear archivo de URLs de la app:** Dentro de la carpeta `frontend_appcafe`, crea un nuevo archivo llamado `urls.py`.

2.  **Definir las URLs para el CRUD:** En `frontend_appcafe/urls.py`, definiremos las rutas para cada acción.

    ```python
    # frontend_appcafe/urls.py
    
    from django.urls import path
    from . import views
    
    urlpatterns = [
        # Read (Leer) - La página principal que muestra todos los cafés
        path('', views.lista_cafes, name='lista_cafes'),
        
        # Create (Crear) - Una página con un formulario para añadir un nuevo café
        path('cafe/nuevo/', views.crear_cafe, name='crear_cafe'),
        
        # Update (Actualizar) - Una página para editar un café existente
        path('cafe/<int:pk>/editar/', views.editar_cafe, name='editar_cafe'),
        
        # Delete (Borrar) - La acción para eliminar un café
        path('cafe/<int:pk>/eliminar/', views.eliminar_cafe, name='eliminar_cafe'),
    ]
    ```

3.  **Crear las Vistas:** Ahora, la parte central de la lógica. Edita `frontend_appcafe/views.py` para que contenga las funciones que acabamos de referenciar.

    ```python
    # frontend_appcafe/views.py
    
    from django.shortcuts import render, redirect, get_object_or_404
    from .models import Cafe
    
    # Vista para mostrar la lista de todos los cafés (Read)
    def lista_cafes(request):
        cafes = Cafe.objects.all()
        return render(request, 'cafe/lista_cafes.html', {'cafes': cafes})
    
    # Vista para crear un nuevo café (Create)
    def crear_cafe(request):
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            precio = request.POST.get('precio')
            stock = request.POST.get('stock')
            imagen_url = request.POST.get('imagen_url')
            
            Cafe.objects.create(nombre=nombre, precio=precio, stock=stock, imagen_url=imagen_url)
            return redirect('lista_cafes')
            
        return render(request, 'cafe/cafe_form.html')
    
    # Vista para editar un café existente (Update)
    def editar_cafe(request, pk):
        cafe = get_object_or_404(Cafe, pk=pk)
        if request.method == 'POST':
            cafe.nombre = request.POST.get('nombre')
            cafe.precio = request.POST.get('precio')
            cafe.stock = request.POST.get('stock')
            cafe.imagen_url = request.POST.get('imagen_url')
            cafe.save()
            return redirect('lista_cafes')
            
        return render(request, 'cafe/cafe_form.html', {'cafe': cafe})
    
    # Vista para eliminar un café (Delete)
    def eliminar_cafe(request, pk):
        cafe = get_object_or_404(Cafe, pk=pk)
        if request.method == 'POST':
            cafe.delete()
            return redirect('lista_cafes')
            
        return render(request, 'cafe/cafe_confirm_delete.html', {'cafe': cafe})
    ```

**Resumen del Punto:** Hemos creado el "cerebro" de nuestra aplicación. Cada URL está asociada a una función (vista) que sabe qué hacer: obtener datos de la base de datos, procesar formularios o eliminar registros, y finalmente, decidir qué página HTML mostrar al usuario.

---

### **Paso 7: Creación de las Plantillas (Templates)**

Aquí es donde crearemos el HTML para dar vida a nuestra interfaz.

1.  **Crea las carpetas de plantillas:**
    *   En la raíz de tu proyecto (junto a `manage.py`), crea una carpeta `templates`.
    *   Dentro de `templates`, crea otra carpeta llamada `cafe`.
    *   *Estructura final:* `templates/cafe/`

2.  **Configura el directorio de plantillas:** En `backend_pcafe/settings.py`, dile a Django dónde buscar esta carpeta.

    ```python
    # backend_pcafe/settings.py
    import os # Asegúrate que `import os` esté al principio del archivo
    
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')], # Modificar esta línea
            'APP_DIRS': True,
            'OPTIONS': {
                # ...
            },
        },
    ]
    ```

3.  **Crea los archivos HTML:**

    *   **`templates/base.html` (Plantilla base con Bootstrap 5)**
        Este archivo será el esqueleto de todas nuestras páginas.

        ```html
        <!doctype html>
        <html lang="es">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>{% block title %}Café Oxxo{% endblock %}</title>
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
          <style>
            body { background-color: #f8f9fa; }
            .card-img-top {
                width: 100%;
                height: 200px;
                object-fit: cover;
            }
          </style>
        </head>
        <body>
          {% include 'partials/navbar.html' %}
          <main class="container mt-4">
            {% block content %}{% endblock %}
          </main>
          {% include 'partials/footer.html' %}
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        ```

    *   **Crea la carpeta `templates/partials/`** para organizar mejor.
    *   **`templates/partials/navbar.html` (Navbar mejorado)**
        Una barra de navegación elegante con un enlace para añadir nuevos cafés.

        ```html
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm">
          <div class="container">
            <a class="navbar-brand fw-bold" href="{% url 'lista_cafes' %}">
              ☕ Café del Oxxo
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                  <a class="btn btn-outline-light" href="{% url 'crear_cafe' %}">Añadir Nuevo Café</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        ```

    *   **`templates/partials/footer.html`**

        ```html
        <footer class="py-4 mt-5 bg-light text-center">
          <div class="container">
            <p class="mb-0 text-muted">&copy; 2024 Mi Tienda de Café. Todos los derechos reservados.</p>
          </div>
        </footer>
        ```

    *   **`templates/cafe/lista_cafes.html` (La vista principal de la imagen)**
        Muestra las tarjetas de café y los botones de acción.

        ```html
        {% extends 'base.html' %}

        {% block title %}Catálogo de Cafés{% endblock %}

        {% block content %}
        <h1 class="mb-4">Nuestro Menú de Cafés</h1>
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4 g-4">
          {% for cafe in cafes %}
          <div class="col">
            <div class="card h-100 shadow-sm">
              <img src="{{ cafe.imagen_url }}" class="card-img-top" alt="{{ cafe.nombre }}">
              <div class="card-body d-flex flex-column">
                <h5 class="card-title">{{ cafe.nombre }}</h5>
                <p class="card-text text-muted">${{ cafe.precio }}</p>
                <div class="mt-auto">
                  <a href="#" class="btn btn-primary w-100 mb-2">Agregar al carrito</a>
                  <div class="d-flex justify-content-between">
                     <a href="{% url 'editar_cafe' cafe.pk %}" class="btn btn-secondary btn-sm">Editar</a>
                     <a href="{% url 'eliminar_cafe' cafe.pk %}" class="btn btn-danger btn-sm">Eliminar</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          {% empty %}
            <p>No hay cafés disponibles en este momento.</p>
          {% endfor %}
        </div>
        {% endblock %}
        ```

    *   **`templates/cafe/cafe_form.html` (Formulario para Crear/Editar)**
        Un formulario reutilizable.

        ```html
        {% extends 'base.html' %}

        {% block title %}{% if cafe %}Editar Café{% else %}Crear Nuevo Café{% endif %}{% endblock %}
        
        {% block content %}
        <div class="row justify-content-center">
            <div class="col-md-8 col-lg-6">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <h2 class="card-title text-center mb-4">{% if cafe %}Editar {{ cafe.nombre }}{% else %}Añadir un Nuevo Café{% endif %}</h2>
                        <form method="post">
                            {% csrf_token %}
                            <div class="mb-3">
                                <label for="nombre" class="form-label">Nombre del Café</label>
                                <input type="text" class="form-control" id="nombre" name="nombre" value="{{ cafe.nombre|default:'' }}" required>
                            </div>
                            <div class="mb-3">
                                <label for="precio" class="form-label">Precio</label>
                                <input type="number" step="0.01" class="form-control" id="precio" name="precio" value="{{ cafe.precio|default:'' }}" required>
                            </div>
                            <div class="mb-3">
                                <label for="stock" class="form-label">Stock (Cantidad disponible)</label>
                                <input type="number" class="form-control" id="stock" name="stock" value="{{ cafe.stock|default:'' }}" required>
                            </div>
                            <div class="mb-3">
                                <label for="imagen_url" class="form-label">URL de la Imagen</label>
                                <input type="url" class="form-control" id="imagen_url" name="imagen_url" value="{{ cafe.imagen_url|default:'' }}" required>
                            </div>
                            <div class="d-grid gap-2">
                                <button type="submit" class="btn btn-primary">Guardar Cambios</button>
                                <a href="{% url 'lista_cafes' %}" class="btn btn-secondary">Cancelar</a>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        {% endblock %}
        ```

    *   **`templates/cafe/cafe_confirm_delete.html` (Confirmación de Borrado)**

        ```html
        {% extends 'base.html' %}
        
        {% block title %}Confirmar Eliminación{% endblock %}
        
        {% block content %}
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card text-center shadow-sm">
                    <div class="card-body">
                        <h2 class="card-title">Confirmar Eliminación</h2>
                        <p>¿Estás seguro de que deseas eliminar el café "<strong>{{ cafe.nombre }}</strong>"?</p>
                        <form method="post">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-danger">Sí, eliminar</button>
                            <a href="{% url 'lista_cafes' %}" class="btn btn-secondary">Cancelar</a>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        {% endblock %}
        ```

---

### **Paso 8: Poblar Datos y Ejecutar el Servidor**

1.  **Crea un superusuario** para acceder al panel de administración de Django:
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para crear un nombre de usuario y contraseña.

2.  **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

3.  **Añade datos:**
    *   Abre tu navegador y ve a `http://127.0.0.1:8000/admin/`.
    *   Inicia sesión con el superusuario que creaste.
    *   Busca "Cafes" y haz clic en "Añadir".
    *   Rellena los datos para algunos cafés. Aquí tienes URLs de imágenes que puedes usar:
        *   `https://images.pexels.com/photos/312418/pexels-photo-312418.jpeg`
        *   `https://images.pexels.com/photos/1235717/pexels-photo-1235717.jpeg`
        *   `https://images.pexels.com/photos/302899/pexels-photo-302899.jpeg`
        *   `https://images.pexels.com/photos/4109744/pexels-photo-4109744.jpeg`

4.  **¡Prueba la aplicación!**
    *   Ve a `http://127.0.0.1:8000/`. Deberías ver la lista de cafés que añadiste.
    *   Prueba el botón "Añadir Nuevo Café", edita un café existente y elimina otro. ¡Toda la funcionalidad CRUD debería estar funcionando!

---

### **Conclusiones Finales**

1.  **Arquitectura Limpia:** Siguiendo la estructura de Django (MVT), hemos creado una aplicación organizada y fácil de mantener. La lógica, los datos y la presentación están completamente separados.
2.  **Poder del ORM:** Hemos interactuado con la base de datos de una manera muy intuitiva y segura gracias al ORM de Django, sin escribir una sola línea de SQL.
3.  **Sistema de Plantillas Robusto:** El motor de plantillas de Django nos permitió crear una base reutilizable (`base.html`), incluir componentes (`navbar.html`) y mostrar datos dinámicos de forma eficiente y segura.
4.  **CRUD Completo:** Has implementado con éxito el ciclo completo de gestión de datos, que es la base de la gran mayoría de las aplicaciones web.
5.  **Potencial de Expansión:** Este proyecto es una base sólida. Desde aquí, podrías añadir un sistema de usuarios, un carrito de compras real, un panel de administración personalizado y mucho más.