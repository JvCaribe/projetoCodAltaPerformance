from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    genero= models.CharField(max_length=50)
    ano= models.CharField(max_length=20)
    duracao= models.CharField(max_length=20)
    poster = models.URLField(blank=True, null=True)
    imdb_id = models.CharField(max_length=20, blank=True, null=True)
    diretor = models.CharField(max_length=100, blank=True, null=True)

