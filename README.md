# 🔐 Gestor de Contraseñas Inteligente (CRUD Backend)

¡Bienvenido al Gestor de Contraseñas Modular! Este software fue desarrollado en Python aplicando las mejores prácticas de la programación modular y estructuras de datos dinámicas. Permite centralizar, buscar, editar y proteger credenciales de forma eficiente en consola.

## 🚀 Características y Arquitectura Básica
El sistema fue migrado de una lógica rudimentaria de listas paralelas a una robusta estructura de **Lista de Diccionarios**, permitiendo una manipulación segura y directa de la memoria sin riesgos de desfasaje de datos.

### 🛠️ Funcionalidades Implementadas (Estructura CRUD):
1. **Create (Alta):** Registro modular mediante funciones independientes que capturan `cuenta`, `usuario` y `contraseña` blindando el sistema contra campos vacíos.
2. **Read (Lectura General y Búsqueda):** - Listado prolijo de todos los registros en memoria mediante f-strings.
   - Algoritmo de **Búsqueda Lineal** optimizado mediante banderas lógicas (interruptores) para localizar cuentas específicas en silencio.
3. **Update (Modificación):** Sobreescritura dinámica de datos directamente sobre las llaves del diccionario seleccionado.
4. **Delete (Baja):** Remoción segura de elementos mediante el método nativo `.remove()` y detención controlada con `break` para resguardar la consistencia de los índices de la lista.

## 💻 Tecnologías Utilizadas
- **Lenguaje:** Python 3.x
- **Estructuras:** Listas, Diccionarios nativos.
- **Flujos de control:** Match-Case (Python 3.10+), Bucles iterativos, Banderas Booleanas.
- **Herramientas de control:** Sanitización de cadenas con `.strip()` y `.title()`.

---
*Desarrollado con fines formativos bajo estándares profesionales de Code Review.*
