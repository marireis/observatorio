from django.contrib import admin
from .models import *

class BolsaAdmin(admin.ModelAdmin):
    model = Bolsa
    list_display = ('pesquisador','programa','pais')

class PesquisadorAdmin(admin.ModelAdmin):
    model = Pesquisador
    list_display = ('nome', 'area_pesquisa')

class InstituicaoAdmin(admin.ModelAdmin):
    model = Instituicao
    list_display = ('nome', 'endereco')

class ProgramaAdmin(admin.ModelAdmin):
    model = Programa
    list_display = ('nome')

admin.site.register(Bolsa, BolsaAdmin)
admin.site.register(Pesquisador, PesquisadorAdmin)
admin.site.register(Programa)
admin.site.register(Instituicao, InstituicaoAdmin)
