from enum import unique
from tabnanny import verbose
from turtle import mode
from django.db import models

# Create your models here.
class Hero(models.Model):
    # Opciones
    
    UNIVERSE_CHOICES=(
        ('1','Marvel'),
        ('2','DC')
    )
    
    # Atributos
    name=models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nombre'
    )
    age=models.IntegerField(
        
    )
    
    universe=models.CharField(
        max_length=1,
        choices=UNIVERSE_CHOICES,
        verbose_name='Universo'
    )
    
    class Meta:
        verbose_name = 'Heroe'
        verbose_name_plural = 'Heroes'
    
    def __str__(self):
        return self.name
    