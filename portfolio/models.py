from django.db import models
from datetime import date


# Create your models here.


class Professor(models.Model):
    nome_prof = models.CharField(max_length=100)
    link_linkedin = models.CharField(max_length=100)
    link_lusofona = models.CharField(max_length=100)
    foto = models.ImageField()

    def __str__(self):
        return self.nome_prof


class Cadeira(models.Model):
    nome_cadeira = models.CharField(max_length=50)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ect = models.IntegerField()
    ranking = models.IntegerField()
    grupo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    imagem = models.ImageField()
    docente_teorica = models.ForeignKey(Professor, related_name='docente_teorica', on_delete=models.CASCADE)
    docente_pratica = models.ForeignKey(Professor, related_name='docente_pratica', on_delete=models.CASCADE)

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


class Projeto(models.Model):
    proj_titulo = models.CharField(max_length=100)
    proj_descricao = models.CharField(max_length=100)
    proj_imagem = models.ImageField()
    proj_ano = models.CharField(max_length=100)
    proj_cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE)

    def __str__(self):
        return self.proj_titulo


class Tecnologia(models.Model):
    tec_nome = models.CharField(max_length=50)
    tec_acronimo = models.CharField(max_length=50)
    tec_ano_criacao = models.CharField(max_length=4)
    tec_logotipo = models.ImageField()
    tec_site_link = models.CharField(max_length=100)
    tec_descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.tec_nome


class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=100)
    link_linkedin = models.CharField(max_length=100)
    link_instagram = models.CharField(max_length=100)
    link_github = models.CharField(max_length=100)
    foto_aluno = models.ImageField()
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_aluno


class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    imagem = models.ImageField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


class Informacao(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo


class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    autor = models.CharField(max_length=200)
    ano = models.IntegerField()
    imagem = models.ImageField()
    github = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo
