from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='artocles/')
    category = models.ForeignKey(
        Category,
        related_name="thing",
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name


class Thing(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    post = models.OneToOneField(
        Post,
        related_name="thing",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=50)
    post = models.ForeignKey(Post, related_name="review", on_delete=models.CASCADE)


class CartThing(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', related_name="user_customer", on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', related_name="cart", on_delete=models.CASCADE)
    thing = models.ForeignKey(Thing, verbose_name='Вещь', related_name='thing', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cost = models.DecimalField(max_digits=7, verbose_name='Общая стоимость', decimal_places=2)

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.thing.name)


class Cart(models.Model):
    own = models.ForeignKey('Customer', verbose_name='Владелец', related_name="cart_customer", on_delete=models.CASCADE)
    thing = models.ManyToManyField(CartThing, blank=True, related_name="cart_thing")
    qty_thing = models.PositiveIntegerField(default=0)
    cost = models.DecimalField(max_digits=7, verbose_name='Общая стоимость', decimal_places=2)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=300, verbose_name='Адрес')

    def __str__(self):
        return "Покупатель: {} (для корзины)".format(self.user.first_name, self.user.last_name)