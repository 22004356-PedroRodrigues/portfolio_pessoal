"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('blog', views.blog_view, name='blog'),
    path('quizz', views.quizz_view, name='quizz'),
    path('educacao', views.educacao_view, name='educacao'),
    path('projetos', views.projetos_view, name='projetos'),
    path('tecnologia', views.tecnologia_view, name='tecnologia'),
    path('contacto', views.contacto_view, name='contacto'),
    path('noticias', views.noticia_view, name='noticias'),
    path('sobre_website', views.sobre_website_view, name='sobre_website'),
    path('editar_noticia/<int:my_id>', views.noticia_form_edit_view, name='editar_noticia'),
    path('nova_noticia', views.noticia_form_new_view, name='nova_noticia'),
    path('eliminar_noticia/<int:my_id>', views.noticia_form_delete_view, name='eliminar_noticia'),
    path('editar_cadeira/<int:my_id>', views.cadeira_form_edit_view, name='editar_cadeira'),
    path('nova_cadeira', views.cadeira_form_new_view, name='nova_cadeira'),
    path('editar_aluno/<int:my_id>', views.aluno_form_edit_view, name='editar_aluno'),
    path('nova_aluno', views.aluno_form_new_view, name='nova_aluno'),
    path('editar_projeto/<int:my_id>', views.projeto_form_edit_view, name='editar_projeto'),
    path('nova_projeto', views.projeto_form_new_view, name='nova_projeto'),
    path('editar_tecnologia/<int:my_id>', views.tecnologia_form_edit_view, name='editar_tecnologia'),
    path('nova_tecnologia', views.tecnologia_form_new_view, name='nova_tecnologia'),
    path('login', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),
]
