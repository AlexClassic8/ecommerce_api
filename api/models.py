from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Modelo de usuario
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name='api_user_set',  # Cambia el related_name para evitar conflictos
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='api_user_permissions_set',  # Cambia el related_name para evitar conflictos
        blank=True
    )
#Modelo de producto
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#Modelo de pedido
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


# Modelo intermedio para los productos en el pedido
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()