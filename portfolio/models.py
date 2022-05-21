from django.db import models
from datetime import date


# Create your models here.

class Cadeira(models.Model):
    nome_cadeira = models.CharField(max_length=50)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ect = models.IntegerField()
    ranking = models.IntegerField()
    grupo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    imagem = models.CharField(max_length=25)

    def __str__(self):
        return self.nome_cadeira


class Post(models.Model):
    nome_pessoa = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=155)
    data = models.DateField(default=date.today())

    def __str__(self):
        return self.nome_pessoa


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50)
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome
