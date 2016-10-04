from django.db import models
from django.contrib.auth.models import User
from enumfields import EnumIntegerField
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport
import parser_breeds


BREEDS = parser_breeds.get_breeds()


class GenderEnum(Enum):
    MALE = 1
    FEMALE = 2

    class Labels:
        MALE = 'Male'
        FEMALE = 'Female'


class OrderStatusEnum(Enum):
    PROCESSING = 1
    SHIPPED = 2
    CLOSED = 3

    class Labels:
        PROCESSING = 'Processing'
        SHIPPED = 'Shipped'
        CLOSED = 'Closed'


class Breed(models.Model):
    name = models.CharField(max_length=50, null=True)
    desc = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name


class CatColor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cat(models.Model):
    breed = models.ForeignKey(Breed)
    sex = EnumIntegerField(GenderEnum)
    cat_color = models.ForeignKey(CatColor)
    date = models.DateField()
    desc = models.CharField(max_length=256, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class Album(models.Model):
    cat = models.ForeignKey(Cat)
    photo = models.ImageField(upload_to='cats')


class Order(models.Model):

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Opened at')
    closed = models.DateTimeField(verbose_name='Closed at',
                                  blank=True,
                                  null=True)
    status = EnumIntegerField(OrderStatusEnum, 
                              default=OrderStatusEnum.PROCESSING)
    customer = models.ForeignKey(User,
                                 blank=True,
                                 null=True)
    phone = models.CharField(max_length=32,
                             null=True)
    address = models.CharField(max_length=256,
                               null=True)
    name = models.CharField(max_length=64,
                            verbose_name='Contact name',
                            null=True)

    def price(self):
        return sum(p.price() for p in self.positions.all())


class OrderPosition(models.Model):

    class Meta:
        verbose_name = 'Order position'
        verbose_name_plural = 'Order positions'

    order = models.ForeignKey(Order, related_name='positions')
    product = models.ForeignKey(Cat)

    def price(self):
        return self.product.price
