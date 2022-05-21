from django import forms
from django.forms import ModelForm
from .models import Post


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
