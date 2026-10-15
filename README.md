# Curso Python — Proyecto práctico de consola

Domina los fundamentos de Python: instalación, sintaxis, tipos de datos, control de flujo, estructuras básicas, modularización, manejo de errores y archivos. Cierra el curso con un proyecto práctico que integra todos los conceptos aprendidos.

Resumen del curso

Vas a construir una aplicación completa de consola en Python dividida en módulos: un sistema interactivo con menús, lógica de decisión y persistencia de datos en archivos de texto. Un ejemplo de proyecto final es una máquina que registra pedidos y guarda la información en archivos.

Estructura recomendada del repositorio

- README.md — descripción del curso (este archivo)
- src/ — código fuente en Python (.py). Aquí irá el `main.py` y los módulos.
- examples/ — ejemplos o scripts ejecutables
- data/ — archivos de texto para persistencia (por ejemplo, pedidos.txt)
- docs/ — material adicional, guías o diapositivas

Etapas del curso

- Etapa 1: Variables iniciales y tipos de datos.
  - Introducción a variables, asignación, números, cadenas, booleanos y conversiones.

- Etapa 2: Control de flujo con condicionales y bucles.
  - if/elif/else, for, while, comprensión de listas y control de flujo.

- Etapa 3: Estructuras de datos para organizar la información.
  - Listas, tuplas, diccionarios, conjuntos y operaciones comunes.

- Etapa 4: Modularización del código en funciones y archivos.
  - Definición de funciones, parámetros, módulos, imports y organización en paquetes simples.

- Etapa 5: Manejo de errores con try/except y persistencia en archivos.
  - Captura de excepciones, uso de context managers (`with`), lectura y escritura en archivos de texto.

- Etapa 6: Integración final de la aplicación desde `main.py`.
  - Integrar menús interactivos, lógica de negocio y persistencia para entregar una aplicación funcional.

Proyecto final (ejemplo)

Construir una "máquina de pedidos" de consola que permita:
- Registrar nuevos pedidos (entrada por teclado).
- Listar pedidos guardados.
- Buscar o filtrar pedidos por criterios simples.
- Guardar y leer pedidos desde un archivo de texto en `data/`.

Requisitos

- Python 3.8 o superior.
- (Opcional) Virtualenv o entorno virtual recomendado.

Cómo empezar

1. Clonar el repositorio:
   git clone https://github.com/crijosmarin/curso-python.git
2. Entrar en la carpeta del proyecto:
   cd curso-python
3. Crear un entorno virtual (opcional):
   python -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate     # Windows
4. Ejecutar el punto de entrada (cuando exista):
   python src/main.py

Contribuciones

Si quieres contribuir con ejercicios, mejoras o correcciones, abre un pull request o crea un issue describiendo tu propuesta.

Licencia

Indica aquí la licencia que prefieras (por ejemplo MIT o CC-BY) o déjalo por defecto hasta que decidas.

Contacto

crijosmarin — añade aquí tu email o perfil si deseas compartirlo.
