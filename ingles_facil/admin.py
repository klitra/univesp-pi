# ingles_facil/admin.py
from django.contrib import admin
from .models import CategoriaDica, Dica

@admin.register(CategoriaDica) # Decorador para registrar o modelo
class CategoriaDicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'cor_card') # Campos exibidos na lista
    prepopulated_fields = {'slug': ('nome',)} # Ajuda a preencher o slug automaticamente a partir do nome

@admin.register(Dica)
class DicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_adicionada', 'link_util')
    list_filter = ('categoria', 'data_adicionada') # Adiciona filtros na lateral
    search_fields = ('titulo', 'conteudo') # Adiciona um campo de busca
from .models import UserProfile, ModuloAprendizado, Tarefa, ProgressoUsuarioTarefa # Adicione os novos modelos

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'pontos_totais', 'get_etapa_crescimento') # Usa o método do modelo

@admin.register(ModuloAprendizado)
class ModuloAprendizadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'ordem', 'pontos_para_desbloquear')
    prepopulated_fields = {'slug': ('titulo',)}

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'modulo', 'ordem', 'pontos_ao_completar')
    list_filter = ('modulo',) # Filtro por módulo
    search_fields = ('titulo', 'conteudo_ou_pergunta')

@admin.register(ProgressoUsuarioTarefa)
class ProgressoUsuarioTarefaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tarefa', 'completada', 'data_conclusao')
    list_filter = ('completada', 'usuario', 'tarefa__modulo') # Filtros úteis
