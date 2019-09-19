from django.db import models

# Create your models here.

class Articulo(models.Model):
	tipo_art = models.CharField(max_length=50)
	talla = models.CharField(max_length=3)
	color = models.CharField(max_length=10)
	fecha_llegada = models.DateField()
	
