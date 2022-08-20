from django.db import models
from django.contrib.auth import get_user_model
from catalog.models import Book

User = get_user_model()


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='carts', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def total_price(self):
        total = 0
        for good in self.goods.all():
            total +=good.price
        return total


class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name='goods')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='goods')
    quantity = models.SmallIntegerField(verbose_name='Quantity')
    price = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name='orders')
    full_name = models.CharField(blank=True, null=True, max_length=60)
    phone = models.IntegerField(blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
