from tabnanny import verbose
from tokenize import Name
from unicodedata import name
from django.db import models
import uuid

# costumer model
class customer(models.Model):
    id         = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    citizen_id = models.PositiveBigIntegerField(verbose_name='citizen_id')
    name       = models.CharField(max_length=100)
    phone      = models.PositiveBigIntegerField(verbose_name='number')
    date       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

# account model
class account(models.Model):
    id           = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    customer     = models.ForeignKey(customer, on_delete=models.CASCADE,related_name='Accounts')
    creation_day = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer}'

