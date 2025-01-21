import random
from faker import Faker
from api.models import Product

# Inicializar Faker para generar datos falsos
fake = Faker()

# Generar 50 productos
for _ in range(50):
    product_name = fake.word().capitalize()  # Genera un nombre aleatorio
    description = fake.sentence()  # Genera una descripción aleatoria
    price = round(random.uniform(10.0, 500.0), 2)  # Precio aleatorio entre 10 y 500
    stock = random.randint(1, 100)  # Stock aleatorio entre 1 y 100

    # Crear un producto en la base de datos
    Product.objects.create(
        name=product_name,
        description=description,
        price=price,
        stock=stock
    )

print("50 productos añadidos correctamente.")