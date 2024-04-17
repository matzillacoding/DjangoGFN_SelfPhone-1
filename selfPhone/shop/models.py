from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
# Enums für die Auswahl der Eigenschaften eines Smartphones


class Manufacturer(models.TextChoices):
    APPLE = 'AP', _('Apple')
    SAMSUNG = 'SM', _('Samsung')
    GOOGLE = 'GO', _('Google')
    SONY = 'SO', _('Sony')
    XIAOMI = 'XI', _('Xiaomi')
    HUAWEI = 'HU', _('Huawei')


class Color(models.TextChoices):
    SCHWARZ = 'Schwarz', _('Schwarz')
    WEISS = 'Weiß', _('Weiß')
    ROT = 'Rot', _('Rot')
    BLAU = 'Blau', _('Blau')
    GRUEN = 'Grün', _('Grün')
    GELB = 'Gelb', _('Gelb')
    GRAU = 'Grau', _('Grau')
    SILBER = 'Silber', _('Silber')
    GOLD = 'Gold', _('Gold')


class Memory_size(models.TextChoices):
    sechs = '6', _('6 GB')
    acht = '8', _('8 GB')
    zwoelf = '12', _('12 GB')
    sechzehn = '16', _('16 GB')


class Storage_size(models.TextChoices):
    einhundertachtundzwanzig = '128', _('128 GB')
    zweihundertsechsundfunfzig = '256', _('256 GB')
    fuenfhundertzwolf = '512', _('512 GB')
    terabyte = '1024', _('1 TB')

#  model für costumer


class Costumer(models.Model):
    costumer = models.OneToOneField(
        User, on_delete=models.CASCADE)  # 1:1 Beziehung zu User
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.first_name + " " + self.last_name


def __str__(self):
    return self.street + " " + self.house_number + ", " + self.postcode + " " + self.city


class Smartphone(models.Model):
    manufacturer = models.CharField(max_length=2, choices=Manufacturer.choices)

    model = models.CharField(max_length=100)

    color = models.CharField(
        max_length=10, choices=Color.choices, default=Color.SCHWARZ)

    prozessortyp = models.CharField(null=True, blank=True, max_length=100)

    ghz = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    cores = models.CharField(null=True, blank=True, max_length=3)

    main_camera = models.CharField(max_length=3, default=0)

    front_camera = models.CharField(max_length=3, default=0)

    display = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    memory_size = models.CharField(
        max_length=2, choices=Memory_size.choices, default=Memory_size.acht)

    storage_size = models.CharField(
        max_length=4, choices=Storage_size.choices, default=Storage_size.einhundertachtundzwanzig)

    akku = models.IntegerField()

    basic_price = models.FloatField(null=True, blank=True, default=0.0)

    picture01 = models.ImageField(null=True, blank=True)

    description = models.TextField(max_length=500)

    picture02 = models.ImageField(null=True, blank=True)

    picture03 = models.ImageField(null=True, blank=True)

    picture04 = models.ImageField(null=True, blank=True)

    def update_price_based_on_specs(self):
        price_adjustments = {
            (Memory_size.sechs, Storage_size.einhundertachtundzwanzig): 0,
            (Memory_size.sechs, Storage_size.zweihundertsechsundfunfzig): 50,
            (Memory_size.sechs, Storage_size.fuenfhundertzwolf): 80,
            (Memory_size.sechs, Storage_size.terabyte): 150,
            (Memory_size.acht, Storage_size.einhundertachtundzwanzig): 30,
            (Memory_size.acht, Storage_size.zweihundertsechsundfunfzig): 80,
            (Memory_size.acht, Storage_size.fuenfhundertzwolf): 100,
            (Memory_size.acht, Storage_size.terabyte): 200,
            (Memory_size.zwoelf, Storage_size.einhundertachtundzwanzig): 50,
            (Memory_size.zwoelf, Storage_size.zweihundertsechsundfunfzig): 100,
            (Memory_size.zwoelf, Storage_size.fuenfhundertzwolf): 150,
            (Memory_size.zwoelf, Storage_size.terabyte): 250,
            (Memory_size.sechzehn, Storage_size.einhundertachtundzwanzig): 80,
            (Memory_size.sechzehn, Storage_size.zweihundertsechsundfunfzig): 130,
            (Memory_size.sechzehn, Storage_size.fuenfhundertzwolf): 180,
            (Memory_size.sechzehn, Storage_size.terabyte): 280,
        }

        self.basic_price += price_adjustments.get(
            (self.memory_size, self.storage_size), 0)

    def save(self, *args, **kwargs):
        self.update_price_based_on_specs()
        super().save(*args, **kwargs)

        if self.picture:

            original_filename, extension = os.path.splitext(self.picture.name)

            self.picture01.name = f"{original_filename}_01{extension}"
            self.picture01.save(self.picture01.name, self.picture.file)

            self.picture02.name = f"{original_filename}_02{extension}"
            self.picture02.save(self.picture02.name, self.picture.file)

            self.picture03.name = f"{original_filename}_03{extension}"
            self.picture03.save(self.picture03.name, self.picture.file)

            self.picture04.name = f"{original_filename}_04{extension}"
            self.picture04.save(self.picture04.name, self.picture.file)

    def __str__(self):
        return f"{self.manufacturer} {self.model} {self.color} {self.memory_size} {self.storage_size}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    smartphone = models.OneToOneField(Smartphone, on_delete=models.CASCADE)


@receiver(post_save, sender=Smartphone)
def update_product(sender, instance, created, **kwargs):
    if created:
        Product.objects.create(smartphone=instance, name=str(instance))
    else:
        product = Product.objects.get(smartphone=instance)
        product.name = str(instance)
        product.save()


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        return self.product.smartphone.basic_price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class Address(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    postcode = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=150)
    house_number = models.CharField(max_length=10)


class Order(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('D', 'Dispatched'),
        ('F', 'Finished'),
    ]

    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)
    timestamp = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='P')

    @property
    def get_total_quantity(self):
        return sum(item.quantity for item in self.products.all())

    @property
    def get_total_price(self):
        total_price = 0
        for item in self.products.all():
            item_price = item.product.smartphone.basic_price
            total_price += item_price * item.quantity
        return total_price

    def __str__(self):
        return f"{self.costumer} {self.address} {self.products.all()}"
