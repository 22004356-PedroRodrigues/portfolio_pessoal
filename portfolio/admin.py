from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Cadeira)
admin.site.register(Post)
admin.site.register(PontuacaoQuizz)
