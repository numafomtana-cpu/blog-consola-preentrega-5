# Blog de Consola - Preentrega 5

## Descripción

Este proyecto consiste en un sistema de blog por consola desarrollado en Python. El objetivo es organizar el código utilizando módulos y paquetes, separando las responsabilidades del sistema.

## Cómo ejecutar el programa

Abrir una terminal en la carpeta raíz del proyecto y ejecutar:

```bash
python main.py
```

## Estructura del proyecto

```text
blog_consola/
├── main.py
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

- **main.py:** inicia el sistema y coordina el menú.
- **blog/datos.py:** contiene los posts, el perfil del autor, los estados y las etiquetas.
- **blog/menu.py:** muestra el menú y recibe la opción del usuario.
- **blog/operaciones.py:** contiene las funciones para listar, buscar y filtrar posts.
- **blog/validaciones.py:** comprueba la estructura y los datos de los posts.
- **blog/__init__.py:** permite reconocer la carpeta blog como paquete de Python.

## Funcionalidades

1. Ver todos los posts.
2. Buscar posts por título.
3. Filtrar posts por tag.
4. Validar los posts.
5. Salir del programa.

Las búsquedas y los filtros ignoran mayúsculas y minúsculas mediante `.lower()`.

## Tecnologías utilizadas

- Python
- Módulos y paquetes
- Funciones
- Listas, diccionarios y sets
- Imports y validaciones