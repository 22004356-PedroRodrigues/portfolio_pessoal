import cloudinary.uploader
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from portfolio.models import *
from portfolio.forms import *
from matplotlib import pyplot as plt
from environs import Env

env = Env()
env.read_env()


def home_page_view(request):
    return render(request, 'portfolio/index.html')


def licenciatura_page_view(request):
    context = {'cadeiras': Cadeira.objects.all(), 'range': range(1, 6)}
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
    cloudinary.config(
        cloud_name=env.str("CLOUD_NAME"),
        api_key=env.str("API_KEY"),
        api_secret=env.str("API_SECRET")
    )
    usernames_y = []
    pontuacao_x = []
    for pontuacao in PontuacaoQuizz.objects.all():
        pontuacao_x.append(pontuacao.pontuacao)
        usernames_y.append(pontuacao.nome)
    pontuacao_x.reverse()
    usernames_y.reverse()
    plt.barh(usernames_y, pontuacao_x)
    plt.savefig('plot.png', bbox_inches='tight')
    cloudinary.uploader.upload('plot.png',
                               public_id="portfolio/sample_id",
                               invalidate=True)
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


@login_required
def cadeira_form_new_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('licenciatura'))

    form = CadeiraForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('licenciatura'))

    context = {'form': form}
    return render(request, 'portfolio/new_edit_delete.html', context)


@login_required
def cadeira_form_edit_view(request, my_id):
    objeto = Cadeira.objects.get(id=my_id)
    form = CadeiraForm(request.POST or None, request.FILES, instance=objeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('licenciatura'))

    context = {'form': form, 'my_id': my_id}
    return render(request, 'portfolio/new_edit_delete.html', context)


@login_required
def aluno_form_new_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('contacto'))

    form = AlunoForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('contacto'))

    context = {'form': form}
    return render(request, 'portfolio/new_edit_delete.html', context)


@login_required
def aluno_form_edit_view(request, my_id):
    objeto = Aluno.objects.get(id=my_id)
    form = AlunoForm(request.POST or None, request.FILES, instance=objeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('licenciatura'))

    context = {'form': form, 'my_id': my_id}
    return render(request, 'portfolio/new_edit_delete.html', context)


@login_required
def projeto_form_new_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('projetos'))

    form = ProjetoForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('projetos'))

    context = {'form': form}
    return render(request, 'portfolio/new_edit_delete.html', context)


@login_required
def projeto_form_edit_view(request, my_id):
    objeto = Projeto.objects.get(id=my_id)
    form = ProjetoForm(request.POST or None, request.FILES, instance=objeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('projetos'))

    context = {'form': form, 'my_id': my_id}
    return render(request, 'portfolio/new_edit_delete.html', context)


@login_required
def tecnologia_form_new_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('tecnologia'))

    form = TecnologiaForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tecnologia'))

    context = {'form': form}
    return render(request, 'portfolio/new_edit_delete.html', context)


@login_required
def tecnologia_form_edit_view(request, my_id):
    objeto = Tecnologia.objects.get(id=my_id)
    form = TecnologiaForm(request.POST or None, request.FILES, instance=objeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tecnologia'))

    context = {'form': form, 'my_id': my_id}
    return render(request, 'portfolio/new_edit_delete.html', context)


@login_required
def noticia_form_new_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('noticias'))

    form = NoticiaForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('noticias'))

    context = {'form': form}
    return render(request, 'portfolio/new_edit_delete.html', context)


@login_required
def noticia_form_edit_view(request, my_id):
    objeto = Noticia.objects.get(id=my_id)
    form = NoticiaForm(request.POST or None, request.FILES, instance=objeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('noticias'))

    context = {'form': form, 'my_id': my_id}
    return render(request, 'portfolio/new_edit_delete.html', context)


@login_required
def cadeira_form_delete_view(request, my_id):
    objeto = Cadeira.objects.get(id=my_id)
    objeto.delete()
    return HttpResponseRedirect(reverse('licenciatura'))


@login_required
def aluno_form_delete_view(request, my_id):
    objeto = Aluno.objects.get(id=my_id)
    objeto.delete()
    return HttpResponseRedirect(reverse('contacto'))


@login_required
def projeto_form_delete_view(request, my_id):
    objeto = Projeto.objects.get(id=my_id)
    objeto.delete()
    return HttpResponseRedirect(reverse('projetos'))


@login_required
def tecnologia_form_delete_view(request, my_id):
    objeto = Tecnologia.objects.get(id=my_id)
    objeto.delete()
    return HttpResponseRedirect(reverse('tecnologia'))


def noticia_form_delete_view(request, my_id):
    objeto = Noticia.objects.get(id=my_id)
    objeto.delete()
    return HttpResponseRedirect(reverse('noticias'))


def view_login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def view_logout(request):
    logout(request)

    return render(request, 'portfolio/index.html', {
        'message': 'Foi desconetado.'
    })


def docente_view(request, my_id):
    objeto = Professor.objects.get(id=my_id)
    context = {'contacto': objeto, 'my_id': my_id}
    return render(request, 'portfolio/docente.html', context)


def tfc_view(request):
    context = {'tfc': TFC.objects.all()}
    return render(request, 'portfolio/tfcs.html', context)
