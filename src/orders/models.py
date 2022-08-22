from django.db import models
from django.contrib.auth import get_user_model
from catalog.models import Book
from django.urls import reverse
import uuid

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
    
    def __str__(self):
        return f'Customer: {self.customer}'


class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name='goods')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='goods')
    quantity = models.SmallIntegerField(verbose_name='Quantity')
    price = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Cart: {self.cart}'


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name='orders')
    full_name = models.CharField(verbose_name="Name and surname of the recipient", max_length=64)
    phone = models.CharField(max_length=16)
    delivery_address = models.CharField(max_length=64)
    comment = models.TextField(verbose_name="Your comments to order", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    STATUS = (
        ('in work', 'in work'),
        ('canceled', 'canceled'),
        ('delivered', 'delivered'),
    )

    status = models.CharField(max_length=9, choices=STATUS, default='in work', help_text='Status of the Order')
    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='customer')

    class Meta:
        ordering = ['created_date']
        permissions = (('can_edit_order', 'Edit order(s)'),) 

            
    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.id} {self.cart.customer}'
