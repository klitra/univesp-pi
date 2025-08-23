# ingles_facil/views.py
from django.shortcuts import render
from .models import CategoriaDica, Dica

def pagina_inicial(request):
    categorias = CategoriaDica.objects.all() # Pega todas as categorias
    ultimas_dicas = Dica.objects.order_by('-data_adicionada')[:5] # Pega as 5 últimas dicas

    context = { # Dados a serem passados para o template
        'titulo_pagina': 'Bem-vindos, Little Owlets!',
        'categorias': categorias,
        'ultimas_dicas': ultimas_dicas,
    }
    # Renderiza o template pagina_inicial.html com os dados do context
    return render(request, 'ingles_facil/pagina_inicial.html', context)

def dicas_por_categoria(request, slug_categoria):
    # Pega a categoria específica pelo slug ou retorna erro 404 se não encontrar
    categoria = CategoriaDica.objects.get(slug=slug_categoria)
    # Filtra as dicas que pertencem a essa categoria
    dicas_da_categoria = Dica.objects.filter(categoria=categoria).order_by('-data_adicionada')
    
    context = {
        'titulo_pagina': f'Dicas sobre {categoria.nome}',
        'categoria': categoria,
        'dicas': dicas_da_categoria,
    }
    return render(request, 'ingles_facil/dicas_por_categoria.html', context)

from django.contrib.auth import logout
from django.shortcuts import redirect
 
def logout_view(request):
    logout(request)
    # Redireciona para uma página após o logoff.
    # Pode ser a página inicial, página de login, etc.
    return redirect('login') # Substitua 'pagina_inicial' pelo nome da sua URL desejada

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect 
from django.contrib.auth import login # Para logar o usuário automaticamente

def cadastro(request):
    if request.user.is_authenticated: # Se o usuário já está logado, redireciona
        return redirect('ingles_facil:pagina_inicial')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Salva o novo usuário
            login(request, user) # Loga o usuário automaticamente
            return redirect('ingles_facil:pagina_inicial') # Redireciona para a página inicial
    else:
        form = UserCreationForm()
    return render(request, 'ingles_facil/cadastro.html', {'form': form, 'titulo_pagina': 'Cadastro de Novo Usuário'})

from django.contrib.auth.decorators import login_required # Para proteger views que exigem login
from .models import ModuloAprendizado, Tarefa, ProgressoUsuarioTarefa, UserProfile # UserProfile já deve estar importado
from django.utils import timezone # Para registrar a data/hora da conclusão
from django.http import HttpResponseForbidden, Http404 # Para erros
from django.shortcuts import get_object_or_404 # Para buscar objetos ou retornar 404
from django.contrib import messages # Para exibir mensagens ao usuário

@login_required # Garante que o usuário esteja logado
def listar_modulos(request):
    # Garante que o perfil exista ou cria um se necessário (robusto)
    perfil_usuario, created = UserProfile.objects.get_or_create(user=request.user)

    
    modulos = ModuloAprendizado.objects.all()
    modulos_com_status = []
    for modulo in modulos:
        is_desbloqueado = perfil_usuario.pontos_totais >= modulo.pontos_para_desbloquear
        tarefas_modulo = Tarefa.objects.filter(modulo=modulo)
        tarefas_completas_modulo_count = ProgressoUsuarioTarefa.objects.filter(
            usuario=request.user, 
            tarefa__in=tarefas_modulo, 
            completada=True
        ).count()
        total_tarefas_modulo = tarefas_modulo.count()
        progresso_percentual = 0
        if total_tarefas_modulo > 0:
            progresso_percentual = (tarefas_completas_modulo_count / total_tarefas_modulo) * 100
        
        modulos_com_status.append({
            'modulo': modulo,
            'is_desbloqueado': is_desbloqueado,
            'tarefas_completas': tarefas_completas_modulo_count,
            'total_tarefas': total_tarefas_modulo,
            'progresso_percentual': progresso_percentual
        })

    context = {
        'titulo_pagina': 'Módulos de Aprendizado',
        'modulos_com_status': modulos_com_status,
        'pontos_usuario': perfil_usuario.pontos_totais,
        'etapa_usuario': perfil_usuario.get_etapa_crescimento(),
    }
    return render(request, 'ingles_facil/listar_modulos.html', context)

@login_required
def detalhe_modulo(request, slug_modulo):
    modulo = get_object_or_404(ModuloAprendizado, slug=slug_modulo)
    perfil_usuario = UserProfile.objects.get(user=request.user) # Perfil já deve existir

    if perfil_usuario.pontos_totais < modulo.pontos_para_desbloquear:
        messages.error(request, f"Você precisa de {modulo.pontos_para_desbloquear} pontos para acessar este módulo. Você tem {perfil_usuario.pontos_totais}.")
        return redirect('ingles_facil:listar_modulos')

    tarefas = Tarefa.objects.filter(modulo=modulo).order_by('ordem')
    tarefas_completadas_ids = ProgressoUsuarioTarefa.objects.filter(
        usuario=request.user, 
        tarefa__in=tarefas, 
        completada=True
    ).values_list('tarefa_id', flat=True) 
    
    context = {
        'titulo_pagina': modulo.titulo,
        'modulo': modulo,
        'tarefas': tarefas,
        'tarefas_completadas_ids': list(tarefas_completadas_ids),
    }
    return render(request, 'ingles_facil/detalhe_modulo.html', context)

@login_required
def completar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    usuario = request.user
    perfil_usuario = UserProfile.objects.get(user=usuario)

    if perfil_usuario.pontos_totais < tarefa.modulo.pontos_para_desbloquear:
        messages.error(request, "Módulo bloqueado! Você não tem pontos suficientes para completar tarefas deste módulo.")
        return redirect('ingles_facil:detalhe_modulo', slug_modulo=tarefa.modulo.slug)

    progresso, created = ProgressoUsuarioTarefa.objects.get_or_create(
        usuario=usuario,
        tarefa=tarefa
    )

    if not progresso.completada: # Se não estava completa ou foi recém-criada (defaults to False se não especificado)
        progresso.completada = True
        progresso.data_conclusao = timezone.now()
        progresso.save()
        
        perfil_usuario.pontos_totais += tarefa.pontos_ao_completar
        perfil_usuario.save()
        messages.success(request, f"Tarefa '{tarefa.titulo}' completada! +{tarefa.pontos_ao_completar} pontos.")
    else:
        messages.info(request, f"Tarefa '{tarefa.titulo}' já havia sido completada.")
    
    return redirect('ingles_facil:detalhe_modulo', slug_modulo=tarefa.modulo.slug)

@login_required
def dashboard_usuario(request):
    perfil_usuario = UserProfile.objects.get(user=request.user) # Perfil já deve existir
    tarefas_completas_count = ProgressoUsuarioTarefa.objects.filter(usuario=request.user, completada=True).count()
    etapa_crescimento = perfil_usuario.get_etapa_crescimento()
    
    context = {
        'titulo_pagina': 'Meu Progresso',
        'pontos_totais': perfil_usuario.pontos_totais,
        'tarefas_completas_count': tarefas_completas_count,
        'etapa_crescimento': etapa_crescimento,
        'usuario': request.user,
    }
    return render(request, 'ingles_facil/dashboard_usuario.html', context)
