from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from portfolio.models import *
from portfolio.forms import *
from matplotlib import pyplot as plt


def home_page_view(request):
    return render(request, 'portfolio/index.html')


def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)


def educacao_view(request):
    return render(request, 'portfolio/timeline.html')


def blog_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PostForm(None)
    context = {'form': form,
               'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def pontuacao_quizz(request):
    pontuacao = 0
    if request.POST['pergunta1'] == 'text-align':
        pontuacao += 20
    if request.POST['pergunta2'] == 'flex':
        pontuacao += 20
    if request.POST['pergunta3'] == 'HyperText Markup Language':
        pontuacao += 20
    if request.POST['pergunta4'] == 'css':
        pontuacao += 20
    if request.POST['pergunta5'] == '<br>':
        pontuacao += 20

    return pontuacao


def quizz_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
        desenha_graficos_resultado(request)
        return render(request, 'portfolio/classificacao.html')
    return render(request, 'portfolio/quizz.html')


def desenha_graficos_resultado(request):
    usernames_y = []
    pontuacao_x = []
    for pontuacao in PontuacaoQuizz.objects.all():
        pontuacao_x.append(pontuacao.pontuacao)
        usernames_y.append(pontuacao.nome)
    pontuacao_x.reverse()
    usernames_y.reverse()
    plt.barh(usernames_y, pontuacao_x)
    plt.savefig('portfolio/static/portfolio/images/plot.png', bbox_inches='tight')
    pass


def projetos_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


def tecnologia_view(request):
    context = {'tecnologias': Tecnologia.objects.all()}
    return render(request, 'portfolio/tecnologia.html', context)


def contacto_view(request):
    context = {'contacto': Aluno.objects.first()}
    return render(request, 'portfolio/perfil_individual.html', context)


def noticia_view(request):
    context = {'noticias': Noticia.objects.all()}
    return render(request, 'portfolio/noticias.html', context)


def sobre_website_view(request):
    context = {'informacaos': Informacao.objects.all()}
    return render(request, 'portfolio/about_website.html', context)
