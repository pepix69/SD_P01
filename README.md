# SD_P01
Práctica 1 de Sistemas Distribuidos: Creación de una API para gestionar datos de una
tienda en línea utilizando MongoDB.

Integrantes: 
José Ángel Montoya Zúñiga
Yavé Emmanuel Vargas Márquez
Rodrigo Olmos Gómez
Martha Dalila Cardona Serna
José Refugio Salinas Uribe


# API de Gestión de Productos, Categorías, Pedidos y Clientes

Esta API está construida con FastAPI y se conecta a una base de datos MongoDB para gestionar productos, categorías, pedidos y clientes. Proporciona operaciones CRUD (Crear, Leer todos, Leer por ID, Actualizar y Eliminar) para cada uno de estos.

Estructura de los Modelos
Producto
{
  "nombre": "string",
  "descripcion": "string",
  "precio": 0.0,
  "stock": 0
}

Categoría
{
  "nombre": "string",
  "descripcion": "string"
}

Pedido
{
  "fecha": "YYYY-MM-DD",
  "total": 0,
  "productos": ["producto_id1", "producto_id2"]
}

Cliente
{
  "nombre": "string",
  "apellido": "string",
  "correo": "string"
}

Endpoints

----------------------------------------------------------------------------------
			Productos
----------------------------------------------------------------------------------
Crear Producto: POST /productos/
	Request Body:
	{
	  "nombre": "Producto A",
	  "descripcion": "Descripción del producto A",
	  "precio": 100.5,
	  "stock": 10
	}
	Response:
	{
	  "message": "El usuario se agrego correctamente"
	}

Obtener todos los Productos: GET /productos/
	Response:
	{
	  "0": {
		"nombre": "Producto A",
		"descripcion": "Descripción del producto A",
		"precio": 100.5,
		"stock": 10
	  },
	  "1": {
		"nombre": "Producto B",
		"descripcion": "Descripción del producto B",
		"precio": 50.0,
		"stock": 5
	  }
	}

Obtener un Producto por ID: GET /productos/{producto_id}
	Response:
	{
	  "nombre": "Producto A",
	  "descripcion": "Descripción del producto A",
	  "precio": 100.5,
	  "stock": 10
	}

Actualizar un Producto: PUT /productos/{producto_id}
	Request Body:
	{
	  "nombre": "Producto A Modificado",
	  "descripcion": "Nueva descripción",
	  "precio": 150.0,
	  "stock": 8
	}
	Response:
	{
	  "nombre": "Producto A Modificado",
	  "descripcion": "Nueva descripción",
	  "precio": 150.0,
	  "stock": 8
	}

Eliminar un Producto: DELETE /productos/{producto_id}
	Response:
	{
	  "message": "Producto eliminado correctamente"
	}

----------------------------------------------------------------------------------
			Categorías
----------------------------------------------------------------------------------
Crear Categoría: POST /categorias/
	Request Body:
	{
	  "nombre": "Categoría X",
	  "descripcion": "Descripción de la categoría X"
	}
	Response:
	{
	  "message": "La categoria se agrego correctamente"
	}

Obtener todas las Categorías: GET /categorias/
	Response:
	{
	  "0": {
		"nombre": "Categoría X",
		"descripcion": "Descripción de la categoría X"
	  },
	  "1": {
		"nombre": "Categoría Y",
		"descripcion": "Descripción de la categoría Y"
	  }
	}

Obtener una Categoría por ID: GET /categorias/{categoria_id}
	Response:
	{
	  "id": "60c72b2f9af1c88b6c7a4b9c",
	  "nombre": "Categoría X",
	  "descripcion": "Descripción de la categoría X"
	}

Actualizar una Categoría: PUT /categorias/{categoria_id}
	Request Body:
	{
	  "nombre": "Categoría X Modificada",
	  "descripcion": "Nueva descripción"
	}
	Response:
	{
	  "nombre": "Categoría X Modificada",
	  "descripcion": "Nueva descripción"
	}

Eliminar una Categoría: DELETE /categorias/{categoria_id}
	Response:
	{
	  "message": "Categoria eliminado correctamente"
	}

----------------------------------------------------------------------------------
			Pedidos
----------------------------------------------------------------------------------
Crear Pedido: POST /pedidos/
	Request Body:
	{
	  "fecha": "2024-09-10",
	  "total": 200,
	  "productos": ["60c72b2f9af1c88b6c7a4b9c", "60c72b3e9af1c88b6c7a4b9d"]
	}
	Response:
	{
	  "fecha": "2024-09-10",
	  "total": 200,
	  "productos": ["60c72b2f9af1c88b6c7a4b9c", "60c72b3e9af1c88b6c7a4b9d"]
	}

Obtener todos los Pedidos: GET /pedidos/
	Response:
	{
	  "0": {
		"fecha": "2024-09-10",
		"total": 200,
		"productos": ["60c72b2f9af1c88b6c7a4b9c", "60c72b3e9af1c88b6c7a4b9d"]
	  },
	  "1": {
		"fecha": "2024-09-11",
		"total": 300,
		"productos": ["60c72b4e9af1c88b6c7a4b9e"]
	  }
	}

Obtener un Pedido por ID: GET /pedidos/{pedido_id}
	Response:
	{
	  "fecha": "2024-09-10",
	  "total": 200,
	  "productos": ["60c72b2f9af1c88b6c7a4b9c", "60c72b3e9af1c88b6c7a4b9d"]
	}

Actualizar un Pedido: PUT /pedidos/{pedido_id}
	Request Body:
	{
	  "fecha": "2024-09-12",
	  "total": 250,
	  "productos": ["60c72b2f9af1c88b6c7a4b9c"]
	}
	Response:
	{
	  "fecha": "2024-09-12",
	  "total": 250,
	  "productos": ["60c72b2f9af1c88b6c7a4b9c"]
	}

Eliminar un Pedido: DELETE /pedidos/{pedido_id}
	Response:
	{
	  "message": "Pedido eliminado correctamente"
	}

----------------------------------------------------------------------------------
Clientes
----------------------------------------------------------------------------------
Crear Cliente: POST /clientes/
	Request Body:
	{
	  "nombre": "Juan",
	  "apellido": "Pérez",
	  "correo": "juan.perez@example.com"
	}
	Response:
	{
	  "id": "60c72b5f9af1c88b6c7a4b9f",
	  "nombre": "Juan",
	  "apellido": "Pérez",
	  "correo": "juan.perez@example.com"
	}

Obtener todos los Clientes: GET /clientes/
	Response:
	[
	  {
		"id": "60c72b5f9af1c88b6c7a4b9f",
		"nombre": "Juan",
		"apellido": "Pérez",
		"correo": "juan.perez@example.com"
	  },
	  {
		"id": "60c72b6f9af1c88b6c7a4b9g",
		"nombre": "Ana",
		"apellido": "García",
		"correo": "ana.garcia@example.com"
	  }
	]

Obtener un Cliente por ID: GET /clientes/{cliente_id}
	Response:
	{
	  "id": "60c72b5f9af1c88b6c7a4b9f",
	  "nombre": "Juan",
	  "apellido": "Pérez",
	  "correo": "juan.perez@example.com"
	}

Actualizar un Cliente: PUT /clientes/{cliente_id}
	Request Body:
	{
	  "nombre": "Juan",
	  "apellido": "Pérez",
	  "correo": "juan.perez@nuevoemail.com"
	}
	Response:
	{
	  "nombre": "Juan",
	  "apellido": "Pérez",
	  "correo": "juan.perez@nuevoemail.com"
	}

Eliminar un Cliente: DELETE /clientes/{cliente_id}
	Response:
	{
	  "message": "Cliente eliminado correctamente"
	}


