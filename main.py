#Crear Apis y manejar exepciones
from fastapi import FastAPI, HTTPException
#importar paquete para crear la estructura de los datos
from pydantic import BaseModel
#Conexion con mongo db
from motor import motor_asyncio
from bson import ObjectId
from datetime import date
from typing import List
#Confgurar la conexion con mongo db
#ubicacion de la conexion de mongo db
MONGO_URI = "mongodb://localhost:27017"
#ejecutarel clinte de bases de datos que es motor
cliente = motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = cliente["practica01"]

productos = db["productos"]
categorias = db["categorias"]
pedidos = db["pedidos"]
clientes = db["clientes"]

#Crear objeto para interactuar con la API
app = FastAPI()

class Producto(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int

class Categoria(BaseModel):
    nombre: str
    descripcion: str

class Pedido(BaseModel):
    fecha: date
    total: int
    productos: List[str]

class Cliente(BaseModel):
    nombre: str
    apellido: str
    correo: str


#-------------------------------------------------------------------------------------------------------------------------
#CRUD Productos
# Create
@app.post("/productos/")
async def create_producto(producto: Producto):
    #seagrega un usuario a la base de datos
    # los datos de usuario deben estar en diccionario
    await productos.insert_one(producto.dict())
    return {
        "message" : "El usuario se agrego correctamente"
    }

# Get All
@app.get("/productos/")
async def get_productos():
    #obtener de manera asincrona todos los usuarios
    resultados = dict()#todos los usuarios
    productos_ = await productos.find().to_list(None)
    #iterar todos los elemneyos de la lista users 
    for i, producto in enumerate(productos_):
        #diccionario por cada usuario
        resultados[i] = dict()
        resultados[i]["nombre"] = producto["nombre"]
        resultados[i]["descripcion"] = producto["descripcion"]
        resultados[i]["precio"] = producto["precio"]
        resultados[i]["stock"] = producto["stock"]
    return resultados

# Get One
@app.get("/productos/{producto_id}")
async def get_producto(producto_id: str):
    # Aquí se busca el usuario y se retorna un diccionario o un objeto User
    producto = await productos.find_one({"_id": ObjectId(producto_id)})
    if producto is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # El modelo User se usa para la respuesta
    return {
        "nombre" : producto["nombre"],
        "descripcion" : producto["descripcion"],
        "precio" : producto["precio"],
        "stock" : producto["stock"]
    }

# Update
@app.put("/users/{producto_id}")
async def update_producto(producto_id: str, producto: Producto):

     # Convertir el ID a ObjectId
    producto_id = ObjectId(producto_id)
    
    # Buscar el usuario para verificar si existe
    existing_user = await productos.find_one({"_id": producto_id})
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Realizar la actualización
    update_result = await productos.update_one(
        {"_id": producto_id},
        {"$set": producto.dict()}  # Usa $set para actualizar los campos específicos
    )
    
     # Obtener el usuario actualizado
    updated_user = await productos.find_one({"_id": producto_id})

    return {
        "nombre" : updated_user["nombre"],
        "descripcion" : updated_user["descripcion"],
        "precio" : updated_user["precio"],
        "stock" : updated_user["stock"]
    }

# Delete
@app.delete("/users/{producto_id}")
async def delete_producto(producto_id: str):
    # Verificar si el id proporcionado es válido
    if not ObjectId.is_valid(producto_id):
        raise HTTPException(status_code=400, detail="ID no válido")

    # Convertir el id a ObjectId y buscar el usuario
    delete_result = await productos.delete_one({"_id": ObjectId(producto_id)})

    # Verificar si se eliminó algún usuario
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return {"message": "Producto eliminado correctamente"}





#-------------------------------------------------------------------------------------------------------------------------

# Categorías CRUD 

# Create Read Update Delete

# Create 
@app.post("/categorias/")
async def create_categorias(categoria: Categoria):
    # Se agrega un usuario en la base de datos
    # Los datos del usuario deben estar en diccionario
    await categorias.insert_one(categoria.dict())
    return {"message: La categoria se agrego correctamente"}

# Get all
@app.get("/categorias/")
async def get_categorias():
    # Obtener de manera asincrona todos los usuarios
    resultados = dict() # Diccionario que tiene todos los usuarios
    users = await categorias.find().to_list(None)
    # Iterar todos los resultados de la lista
    for i, user in enumerate(users):
        
        resultados[i] = dict()
        resultados[i]["nombre"] = user["nombre"]
        resultados[i]["descripcion"] = user["descripcion"]
    return resultados


# Read / Get
@app.get("/categorias/{categoria_id}")
async def get_categoria(categoria_id: str):
    # Aquí se busca el usuario y se retorna un diccionario o un objeto User
    user = await categorias.find_one({"_id": ObjectId(categoria_id)})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    

    # El modelo User se usa para la respuesta
    return {
        "id" : str(categorias["_id"]),
        "nombre" : categorias["nombre"],
        "descripcion" : categorias["descripcion"]
    }


# Update
@app.put("/categorias/{categoria_id}")
async def update_categoria(categoria_id: str, categoria: Categoria):

     # Convertir el ID a ObjectId
    categoria_id = ObjectId(categoria_id)
    
    # Buscar el usuario para verificar si existe
    existing_user = await categorias.find_one({"_id": categoria_id})
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Realizar la actualización
    update_result = await categorias.update_one(
        {"_id": categoria_id},
        {"$set": categoria.dict()}  # Usa $set para actualizar los campos específicos
    )
    
     # Obtener el usuario actualizado
    updated_user = await categorias.find_one({"_id": categoria_id})

    return {
        "nombre" : updated_user["nombre"],
        "descripcion" : updated_user["descripcion"]
    }

# Delete
@app.delete("/categorias/{categoria_id}")
async def delete_user(categoria_id: str):
    # Verificar si el id proporcionado es válido
    if not ObjectId.is_valid(categoria_id):
        raise HTTPException(status_code=400, detail="ID no válido")

    # Convertir el id a ObjectId y buscar el usuario
    delete_result = await categorias.delete_one({"_id": ObjectId(categoria_id)})

    # Verificar si se eliminó algún usuario
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Categoria no encontrado")

    return {"message": "Categoria eliminado correctamente"}


#-------------------------------------------------------------------------------------------------------------------------
# Pedido CRUD 
# Create
@app.post("/pedidos/")
async def create_pedido(pedido: Pedido):
    new_pedido = await pedidos.insert_one(pedido.dict())
    created_pedido = await pedidos.find_one({"_id": new_pedido.inserted_id})
    return {
        "fecha": created_pedido["fecha"],
        "total": created_pedido["total"],
        "productos" : created_pedido["productos"]
    }

# Get All
@app.get("/pedidos/")
async def get_pedidos():
    pedidosAux = dict()
    pedidos_temp = await pedidos.find().to_list(None)

    #iterar todos los resultados de la lista
    for i, pedidos_i in enumerate(pedidos_temp):
        pedidosAux[i] = dict()
        pedidosAux[i]["fecha"] = pedidos_i["fecha"]
        pedidosAux[i]["total"] = pedidos_i["total"]
        pedidosAux[i]["productos"] = pedidos_i["productos"]
    return pedidosAux

# Get One
@app.get("/pedidos/{pedido_id}")
async def get_pedido(pedido_id: str):
    # Aquí se busca el usuario y se retorna un diccionario o un objeto pedido
    pedido = await pedidos.find_one({"_id": ObjectId(pedido_id)})
    if pedido is None:
        raise HTTPException(status_code=404, detail="pedido not found")
    # El modelo pedido se usa para la respuesta
    return {
        "fecha" : pedido["fecha"],
        "total" : pedido["total"],
        "productos" : pedido["productos"]
    }

# Update
@app.put("/pedidos/{pedido_id}")
async def update_pedido(pedido_id: str, pedido: Pedido):

     # Convertir el ID a ObjectId
    pedido_id = ObjectId(pedido_id)
    
    # Buscar el pedido para verificar si existe
    existing_pedido = await pedidos.find_one({"_id": pedido_id})
    if existing_pedido is None:
        raise HTTPException(status_code=404, detail="pedido not found")
    
    # Realizar la actualización
    update_result = await pedidos.update_one(
        {"_id": pedido_id},
        {"$set": pedido.dict()}  # Usa $set para actualizar los campos específicos
    )
    
     # Obtener el producto actualizado
    updated_pedido = await pedidos.find_one({"_id": pedido_id})

    return {
        "fecha" : updated_pedido["fecha"],
        "total" : updated_pedido["total"],
        "productos" : updated_pedido["productos"]
    }

# Delete
@app.delete("/pedidos/{pedido_id}")
async def delete_pedido(pedido_id: str):
    if not ObjectId.is_valid(pedido_id):
        raise HTTPException(status_code=400, detail="ID no válido")
    
    delete_result = await pedidos.delete_one({"_id": ObjectId(pedido_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="pedido no encontrado")
    
    return {"message": "Pedido eliminado correctamente"}


#-------------------------------------------------------------------------------------------------------------------------
# Cliente CRUD 

# Create
@app.post("/clientes/")
async def create_cliente(cliente: Cliente):
    new_cliente = await clientes.insert_one(cliente.dict())
    created_cliente = await clientes.find_one({"_id": new_cliente.inserted_id})
    return {"id": str(created_cliente["_id"]), "nombre": created_cliente["nombre"], "apellido": created_cliente["apellido"], "correo": created_cliente["correo"]}

# Get All
@app.get("/clientes/")
async def get_clientes():
    clientesAux = await clientes.find().to_list(None)
    return [{"id": str(cliente["_id"]), "nombre": cliente["nombre"], "apellido": cliente["apellido"], "correo": cliente["correo"]} for cliente in clientesAux]

# Get One
@app.get("/clientes/{cliente_id}")
async def get_cliente(cliente_id: str):
    cliente = await clientes.find_one({"_id": ObjectId(cliente_id)})
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"id": str(cliente["_id"]), "nombre": cliente["nombre"], "apellido": cliente["apellido"], "correo": cliente["correo"]}

# Update
@app.put("/clientes/{cliente_id}")
async def update_cliente(cliente_id: str, cliente: Cliente):
    cliente_id = ObjectId(cliente_id)
    existing_cliente = await clientes.find_one({"_id": cliente_id})
    if existing_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    await clientes.update_one({"_id": cliente_id}, {"$set": cliente.dict()})
    updated_cliente = await clientes.find_one({"_id": cliente_id})
    return {"id": str(updated_cliente["_id"]), "nombre": updated_cliente["nombre"], "apellido": updated_cliente["apellido"], "correo": updated_cliente["correo"]}

# Delete
@app.delete("/clientes/{cliente_id}")
async def delete_cliente(cliente_id: str):
    if not ObjectId.is_valid(cliente_id):
        raise HTTPException(status_code=400, detail="ID no válido")
    
    delete_result = await clientes.delete_one({"_id": ObjectId(cliente_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return {"message": "Cliente eliminado correctamente"}