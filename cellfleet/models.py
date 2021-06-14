from django.db import models
from django.core.validators import MinValueValidator


class Supplier(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    POSITION_CHOICES = [
        ('President', 'President'),
        ('Director', 'Director'),
        ('Manager', 'Manager'),
        ('Specialist', 'Specialist'),
        ('Referent', 'Referent')
    ]
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    mpk = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, null=True)

    def __str__(self):
        return str(self.id) + " " + self.second_name + " " + self.first_name + " " + self.position


class Device(models.Model):
    mark = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    warranty = models.DateField(null=True, blank=True, auto_now=None)
    delivery_date = models.DateField(null=True, auto_now=None, blank=False)
    event_date = models.DateTimeField(auto_now_add=False, auto_now=True, blank=False)
    user = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.mark + " " + self.model + " /SN: " + self.serial_number


class MobileNumber(models.Model):
    TARIFF_CHOICES = [
        ('VC', 'voice'),
        ('DT', 'data'),
    ]
    number = models.DecimalField(max_digits=9, decimal_places=0, validators=[MinValueValidator(100000000)], unique=True)
    sim = models.CharField(max_length=255, unique=True)
    pin = models.DecimalField(max_digits=4, decimal_places=0)
    puk = models.DecimalField(max_digits=8, decimal_places=0)
    tariff = models.CharField(max_length=3, choices=TARIFF_CHOICES, null=True)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)
    event_date = models.DateTimeField(auto_now_add=False, auto_now=True, blank=False)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)





