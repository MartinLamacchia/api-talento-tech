from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- Configuración de CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Datos de productos ---
products = [
    {
        "id": 1,
        "name": "Joystick para PS4",
        "description": "Joystick inalámbrico para PS4 con diseño ergonómico, vibración y sensores precisos para una experiencia de juego envolvente.",
        "category": "accesorios",
        "price": 5400,
        "stock": 3,
        "image": "./images/products/product1.png",
        "amountToCart": 0
    },
    {
        "id": 2,
        "name": "Joystick para PC",
        "description": "Joystick para PC con diseño ergonómico, conexión USB y gran precisión para disfrutar tus juegos favoritos al máximo.",
        "category": "accesorios",
        "price": 3200,
        "stock": 5,
        "image": "./images/products/product2.png",
        "amountToCart": 0
    },
    {
        "id": 3,
        "name": "Teclado Mecanico",
        "description": "Teclado mecánico con retroiluminación, respuesta rápida y durabilidad ideal para gaming y escritura intensiva.",
        "category": "accesorios",
        "price": 15400,
        "stock": 2,
        "image": "./images/products/product3.png",
        "amountToCart": 0
    },
    {
        "id": 4,
        "name": "Monitor 28''",
        "description": "Monitor de 28'' con resolución nítida, ideal para trabajo, gaming y entretenimiento en alta definición.",
        "category": "monitor",
        "price": 35000,
        "stock": 2,
        "image": "./images/products/product4.png",
        "amountToCart": 0
    },
    {
        "id": 5,
        "name": "Placa de video",
        "description": "Placa de video de alto rendimiento ideal para gaming, edición y diseño, con gráficos fluidos y gran potencia visual.",
        "category": "placa de video",
        "price": 155000,
        "stock": 1,
        "image": "./images/products/product5.png",
        "amountToCart": 0
    },
    {
        "id": 6,
        "name": "Laptod DELL",
        "description": "Laptop DELL confiable y potente, ideal para trabajo, estudio y uso diario con gran rendimiento y diseño elegante.",
        "category": "computadora",
        "price": 254000,
        "stock": 4,
        "image": "./images/products/product6.png",
        "amountToCart": 0
    },
    {
        "id": 7,
        "name": "Motorola e15",
        "description": "Celular motorola e 15",
        "category": "celular",
        "price": 134000,
        "stock": 3,
        "image": "./images/products/product7.png",
        "amountToCart": 0
    },
    {
        "id": 8,
        "name": "Samsung A06",
        "description": "Celular Samsung A06",
        "category": "celular",
        "price": 104000,
        "stock": 5,
        "image": "./images/products/product8.png",
        "amountToCart": 0
    },
    {
        "id": 9,
        "name": "Samsung A56",
        "description": "Celular Samsung A56",
        "category": "celular",
        "price": 224000,
        "stock": 8,
        "image": "./images/products/product9.png",
        "amountToCart": 0
    }
]

# --- Ruta raíz ---
@app.get("/")
def index():
    return {"message": "API FastAPI funcionando correctamente"}

# --- Ruta de productos ---
@app.get("/products")
def get_products():
    return products


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # CORS (opcional si usás frontend local)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # o tu frontend: ["http://127.0.0.1:5500"]
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# def index():
#     return {"message": "Hola Mundo"}