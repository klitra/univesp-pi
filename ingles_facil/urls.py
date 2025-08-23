   # ingles_facil/urls.py
from django.urls import path
from . import views # Importa as views do app atual (ingles_facil)

app_name = 'ingles_facil' # Define um namespace para evitar conflito de nomes de URL entre apps

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'), # URL da página inicial
    # <slug:slug_categoria> captura parte da URL e passa como argumento para a view
    path('categoria/<slug:slug_categoria>/', views.dicas_por_categoria, name='dicas_por_categoria'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('modulos/', views.listar_modulos, name='listar_modulos'),
    path('modulo/<slug:slug_modulo>/', views.detalhe_modulo, name='detalhe_modulo'),
    path('tarefa/completar/<int:tarefa_id>/', views.completar_tarefa, name='completar_tarefa'),
    path('meu-progresso/', views.dashboard_usuario, name='dashboard_usuario'),
    path('logout/', views.logout_view, name='logout'),


]