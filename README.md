# gestor_de_contreasenas
Un sistema de consola robusto y profesional desarrollado en Python para la gestión segura de credenciales de usuario. Este proyecto simula un entorno real de administración de datos aplicando arquitecturas de datos avanzadas e interactividad dinámica.

# 🔐 Gestor de Contraseñas Interactivo (Password Manager)

Un sistema de consola robusto y profesional desarrollado en Python para la gestión segura de credenciales de usuario. Este proyecto simula un entorno real de administración de datos aplicando arquitecturas de datos avanzadas e interactividad dinámica.

## 🚀 Características del Proyecto

- **Menú Dinámico e Interactivo:** Implementación moderna de control de flujo mediante estructuras `match...case` (Python 3.10+).
- **Estructura de Datos Profesional:** Migración de listas paralelas tradicionales a una arquitectura optimizada de **Lista de Diccionarios**, garantizando la sincronización absoluta de cada credencial (Cuenta, Usuario y Contraseña).
- **Sanitización y Validación Defensiva:** Control estricto de entradas de usuario utilizando métodos como `.strip()` y `.title()` para prevenir anomalías en la base de datos, junto con filtros reactivos que impiden el registro de campos vacíos.

## 🛠️ Tecnologías y Conceptos Aplicados

- **Lenguaje:** Python 3.x
- **Estructuras de Control:** Bucles `while True`, condicionales anidados, control de flujo con `continue`.
- **Colecciones Avanzadas:** Estructuras mutables de tipo diccionario (`dict`) embebidas dentro de colecciones de tipo lista (`list`).

## 📁 Estructura de Datos Interna

Cada registro es empaquetado de manera independiente en un diccionario clave-valor y almacenado secuencialmente:

```python
manager = [
    {
        "usuario": "mail@ejemplo.com",
        "cuenta": "Netflix",
        "contrasena": "clave123"
    }
]
