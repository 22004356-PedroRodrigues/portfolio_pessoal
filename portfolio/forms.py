from django import forms
from django.forms import ModelForm
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome_pessoa': forms.TextInput(attrs={'placeholder': 'Kim Metnoku'}),
            'titulo': forms.TextInput(attrs={'placeholder': 'Projeto de programação'}),
            'descricao': forms.Textarea(
                attrs={'size': '150', 'width': '100%', 'rows': '5', 'wrap': 'soft', 'maxlenght': '150',
                       'style': 'width: 95%'}),
            'data': forms.HiddenInput(),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome_pessoa': 'Nome',
            'titulo': 'Título',
            'descricao': 'Descrição',
            'data': 'Data'
        }

    # texto auxiliar a um determinado campo do formulário
    help_texts = {
        'nome_pessoa': 'indique o seu nome',
        'titulo': 'indique qual o projeto em que trabalhou comigo',
        'descricao': 'indique até 155 caracteres como foi a experiência'
    }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'
        # texto a exibir junto à janela de inserção
        labels = {
            'nome_cadeira': 'Nome',
            'ano': 'Ano',
            'semestre': 'Semestre',
            'ranking': 'Raking',
            'grupo': 'Grupo',
            'descricao': 'Descricao',
            'imagem': 'Imagem',
            'docente_teorica': 'Docente Teórica',
            'docente_pratica': 'Docente Prática'
        }


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        # texto a exibir junto à janela de inserção
        labels = {
            'nome_aluno': 'Nome',
            'link_linkedin': 'Link Linkedin',
            'link_instagram': 'Link Instragram',
            'link_github': 'Link Github',
            'foto_aluno': 'Fotografia',
            'cidade': 'Cidade'
        }


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        # texto a exibir junto à janela de inserção
        labels = {
            'proj_titulo': 'Título',
            'proj_descricao': 'Descrição',
            'proj_imagem': 'Imagem',
            'proj_ano': 'Ano',
            'proj_cadeira': 'Cadeira'
        }


class TecnologiaForm(ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'
        # texto a exibir junto à janela de inserção
        labels = {
            'tec_nome': 'Nome',
            'tec_acronimo': 'Acrónimo',
            'tec_ano_criacao': 'Data Criação',
            'tec_logotipo': 'Logótipo',
            'tec_site_link': 'Link',
            'tec_descricao': 'Descrição'
        }


class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'imagem': 'Imagem',
            'link': 'Link',
        }
