Claro, aquí tienes el `README.md` completo en formato texto plano, manteniendo el formato Markdown para que puedas copiarlo y pegarlo:

```
# API REST con Flask y MySQL

Esta API RESTful está construida con Flask y MySQL. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos MySQL para gestionar registros.

## Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
  - [Endpoints](#endpoints)
  - [Ejemplos de Solicitudes y Respuestas](#ejemplos-de-solicitudes-y-respuestas)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Requisitos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados:

- Python 3.x
- MySQL Server
- pip (para instalar dependencias de Python)

## Instalación

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/oyujra/python-crud-flack-api.git
   cd tu_repositorio
   ```

2. **Crea un entorno virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instala las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura el archivo `config.py`**

   Crea un archivo `config.py` en el directorio raíz del proyecto con la siguiente estructura, reemplazando los valores con tus credenciales de MySQL:

   ```python
   class Config:
       MYSQL_HOST = 'localhost'
       MYSQL_USER = 'tu_usuario'
       MYSQL_PASSWORD = 'tu_contraseña'
       MYSQL_DB = 'jiskasoft'
   ```

5. **Crea la base de datos y la tabla**

   Usa el siguiente script SQL para crear la tabla `registros` en tu base de datos MySQL:

   ```sql
   CREATE TABLE `registros` (
     `id_registro` int(11) NOT NULL AUTO_INCREMENT,
     `estado` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
     `id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
     `matricula` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
     `razon_social` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
     `cod_estado_actualizacion` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
     `cod_departamento` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
     `id_establecimiento` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
     `direccion` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
     `respuesta_json` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
     `fecha_insercion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (`id_registro`) USING BTREE,
     INDEX `idx_matricula`(`matricula`) USING BTREE,
     INDEX `idx_id`(`id`) USING BTREE
   ) ENGINE = InnoDB AUTO_INCREMENT = 345730 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;
   ```

## Configuración

Configura el archivo `config.py`: Asegúrate de actualizar el archivo `config.py` con los datos correctos de tu base de datos MySQL.

Archivos de configuración: Puedes ajustar la configuración de Flask y MySQL en `config.py`.

## Uso

### Inicia la aplicación

Ejecuta el siguiente comando para iniciar el servidor Flask:

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`.

### Endpoints disponibles

#### Obtener todos los registros con paginación

- **Método**: GET
- **Ruta**: `/registros?page=<numero_de_pagina>&per_page=<registros_por_pagina>`

**Respuesta JSON de ejemplo**:

```json
{
    "page": 1,
    "per_page": 2,
    "total_records": 5,
    "total_pages": 3,
    "registros": [
        {
            "id_registro": 1,
            "estado": "Activo",
            "id": "12345",
            "matricula": "ABC123",
            "razon_social": "Empresa A",
            "cod_estado_actualizacion": "E001",
            "cod_departamento": "D001",
            "id_establecimiento": "E001",
            "direccion": "Calle 1, Ciudad",
            "respuesta_json": "{\"status\":\"success\"}",
            "fecha_insercion": "2024-08-13 10:00:00"
        },
        {
            "id_registro": 2,
            "estado": "Inactivo",
            "id": "67890",
            "matricula": "XYZ789",
            "razon_social": "Empresa B",
            "cod_estado_actualizacion": "E002",
            "cod_departamento": "D002",
            "id_establecimiento": "E002",
            "direccion": "Calle 2, Ciudad",
            "respuesta_json": "{\"status\":\"error\"}",
            "fecha_insercion": "2024-08-13 11:00:00"
        }
    ]
}
```

#### Obtener un registro específico

- **Método**: GET
- **Ruta**: `/registros/<id_registro>`

**Respuesta JSON de ejemplo**:

```json
{
    "id_registro": 1,
    "estado": "Activo",
    "id": "12345",
    "matricula": "ABC123",
    "razon_social": "Empresa A",
    "cod_estado_actualizacion": "E001",
    "cod_departamento": "D001",
    "id_establecimiento": "E001",
    "direccion": "Calle 1, Ciudad",
    "respuesta_json": "{\"status\":\"success\"}",
    "fecha_insercion": "2024-08-13 10:00:00"
}
```

**Si no se encuentra el registro**:

```json
{
    "error": "Registro no encontrado"
}
```

#### Crear un nuevo registro

- **Método**: POST
- **Ruta**: `/registros`

**Cuerpo de la solicitud (JSON)**:

```json
{
    "estado": "Activo",
    "id": "54321",
    "matricula": "LMN456",
    "razon_social": "Empresa C",
    "cod_estado_actualizacion": "E003",
    "cod_departamento": "D003",
    "id_establecimiento": "E003",
    "direccion": "Calle 3, Ciudad",
    "respuesta_json": "{\"status\":\"created\"}"
}
```

**Respuesta JSON de ejemplo**:

```json
{
    "message": "Registro creado exitosamente"
}
```

#### Actualizar un registro existente

- **Método**: PUT
- **Ruta**: `/registros/<id_registro>`

**Cuerpo de la solicitud (JSON)**:

```json
{
    "estado": "Inactivo",
    "id": "12345",
    "matricula": "ABC123",
    "razon_social": "Empresa A Actualizada",
    "cod_estado_actualizacion": "E004",
    "cod_departamento": "D004",
    "id_establecimiento": "E004",
    "direccion": "Calle 4, Ciudad",
    "respuesta_json": "{\"status\":\"updated\"}"
}
```

**Respuesta JSON de ejemplo**:

```json
{
    "message": "Registro actualizado exitosamente"
}
```

#### Eliminar un registro

- **Método**: DELETE
- **Ruta**: `/registros/<id_registro>`

**Respuesta JSON de ejemplo**:

```json
{
    "message": "Registro eliminado exitosamente"
}
```

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Realiza un fork del repositorio.
2. Crea una rama para tus cambios (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y confirma (`git commit -am 'Agrega nueva funcionalidad'`).
4. Envía tus cambios a tu repositorio (`git push origin feature/nueva-funcionalidad`).
5. Crea un Pull Request en el repositorio original.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

¡Gracias por usar la API! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue en el repositorio.
```

Este texto está listo para ser copiado y pegado en tu archivo `README.md` en GitHub y debería mantener el formato Markdown correctamente.
