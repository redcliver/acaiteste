from django.db import models

# Create your models here.
class senha(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    def __str__(self):
        return str(self.numero)