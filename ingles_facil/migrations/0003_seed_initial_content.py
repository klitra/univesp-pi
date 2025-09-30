
 
from django.db import migrations
from django.utils.text import slugify
 
# Função para popular os dados
def seed_data(apps, schema_editor):
    # Obtenha os modelos da versão histórica correta
    CategoriaDica = apps.get_model('ingles_facil', 'CategoriaDica')
    Dica = apps.get_model('ingles_facil', 'Dica')
    ModuloAprendizado = apps.get_model('ingles_facil', 'ModuloAprendizado')
    Tarefa = apps.get_model('ingles_facil', 'Tarefa')
 
    # --- CATEGORIAS DE DICAS E DICAS ---
 
    # Categoria: Canais do YouTube
    cat_youtube, created = CategoriaDica.objects.get_or_create(
        nome='Canais do YouTube para Aprender Inglês',
        defaults={
            'slug': slugify('Canais do YouTube para Aprender Inglês'),
            'descricao_breve': 'Descubra os melhores canais no YouTube para turbinar seu aprendizado de inglês com vídeos divertidos e didáticos.',
            'cor_card': '#FF0000'
        }
    )
    Dica.objects.get_or_create(
        categoria=cat_youtube,
        titulo='BBC Learning English',
        defaults={
            'conteudo': 'O canal da BBC oferece uma variedade incrível de lições curtas, notícias explicadas e dicas de gramática e pronúncia. Ideal para todos os níveis. Apresenta sotaque britânico predominante.',
'link_util': 'https://www.youtube.com/user/bbclearningenglish'
        }
    )
    Dica.objects.get_or_create(
        categoria=cat_youtube,
        titulo='English with Lucy',
        defaults={
            'conteudo': 'Lucy é uma professora britânica carismática que foca em pronúncia, vocabulário avançado e diferenças culturais. Ótimo para quem quer soar mais natural.',
'link_util': 'https://www.youtube.com/c/EnglishwithLucy'
        }
    )
    Dica.objects.get_or_create(
        categoria=cat_youtube,
        titulo="Rachel's English",
        defaults={
            'conteudo': 'Especializado em pronúncia do inglês americano. Rachel detalha os sons, entonação e ritmo da fala, ajudando a reduzir o sotaque e melhorar a compreensão auditiva.',
'link_util': 'https://www.youtube.com/c/rachelsenglish'
        }
    )
 
    # Categoria: Séries e Filmes
    cat_series_filmes, created = CategoriaDica.objects.get_or_create(
        nome='Séries e Filmes para Aprender Inglês',
        defaults={
            'slug': slugify('Séries e Filmes para Aprender Inglês'),
            'descricao_breve': 'Aprenda inglês de forma divertida e imersiva assistindo a séries e filmes populares.',
            'cor_card': '#1DA1F2'
        }
    )
    Dica.objects.get_or_create(
        categoria=cat_series_filmes,
        titulo='Friends (a série)',
        defaults={'conteudo': 'Um clássico para aprender inglês coloquial e expressões do dia a dia. Os diálogos são relativamente simples e o humor ajuda na memorização. Comece com legendas em português, depois inglês, e por fim, sem legendas!'}
    )
    Dica.objects.get_or_create(
        categoria=cat_series_filmes,
        titulo='Filmes da Pixar/Disney (animações)',
        defaults={'conteudo': 'Animações geralmente têm linguagem clara e vocabulário acessível, além de serem visualmente ricas, o que ajuda na compreensão. Ótimo para iniciantes e intermediários.'}
    )
 
    # Categoria: Músicas
    cat_musicas, created = CategoriaDica.objects.get_or_create(
        nome='Músicas para Aprender Inglês',
        defaults={
            'slug': slugify('Músicas para Aprender Inglês'),
            'descricao_breve': 'Melhore seu vocabulário, pronúncia e ritmo no inglês curtindo suas músicas favoritas.',
            'cor_card': '#1DB954'
        }
    )
    Dica.objects.get_or_create(
        categoria=cat_musicas,
        titulo='The Beatles (banda)',
        defaults={'conteudo': 'As letras das músicas dos Beatles são geralmente claras, poéticas e usam um vocabulário fundamental. Ótimas para cantar junto e aprender construções frasais.'}
    )
    Dica.objects.get_or_create(
        categoria=cat_musicas,
        titulo='LyricsTraining (site/app)',
        defaults={
            'conteudo': 'Uma ferramenta fantástica que transforma o aprendizado com músicas em um jogo. Você completa as letras das músicas enquanto elas tocam. Diversos níveis de dificuldade.',
'link_util': 'https://lyricstraining.com/'
        }
    )
 
    # --- MÓDULOS DE APRENDIZADO E TAREFAS (Estilo Duolingo) ---
 
    # Módulo 1: Primeiros Passos no Inglês
    mod1, created = ModuloAprendizado.objects.get_or_create(
        titulo='Primeiros Passos no Inglês',
        defaults={
            'slug': slugify('Primeiros Passos no Inglês'),
            'descricao': 'Comece sua jornada no inglês aprendendo o básico para se comunicar.',
            'ordem': 1,
            'pontos_para_desbloquear': 0
        }
    )
    Tarefa.objects.get_or_create(
        modulo=mod1,
        titulo='Saudações e Despedidas',
        defaults={
            'conteudo_ou_pergunta': "Aprenda as saudações mais comuns!\n- Hello / Hi (Olá)\n- Good morning (Bom dia)\n- Good afternoon (Boa tarde)\n- Good evening (Boa noite - ao chegar)\n- Good night (Boa noite - ao se despedir/ir dormir)\n- Goodbye / Bye (Tchau)\n- See you later (Até logo)\n\nComo se diz \"Bom dia\" em inglês?",
            'pontos_ao_completar': 10,
            'ordem': 1
        }
    )
    Tarefa.objects.get_or_create(
        modulo=mod1,
        titulo='O Alfabeto Inglês',
        defaults={
            'conteudo_ou_pergunta': 'Assista a um vídeo sobre o alfabeto em inglês e pratique a pronúncia de cada letra. Após assistir, soletre seu nome em inglês para um amigo ou em voz alta.',
            'pontos_ao_completar': 15,
            'ordem': 2
        }
    )
    Tarefa.objects.get_or_create(
        modulo=mod1,
        titulo='Apresentando-se: Meu nome é...',
        defaults={
            'conteudo_ou_pergunta': "Para se apresentar, você pode dizer:\n- My name is [seu nome]. (Meu nome é [seu nome].)\n- I am [seu nome]. (Eu sou [seu nome].)\n\nQual frase usar para dizer seu nome?",
            'pontos_ao_completar': 10,
            'ordem': 3
        }
    )
 
    # Módulo 2: Vocabulário do Dia a Dia
    mod2, created = ModuloAprendizado.objects.get_or_create(
        titulo='Vocabulário do Dia a Dia',
        defaults={
            'slug': slugify('Vocabulário do Dia a Dia'),
            'descricao': 'Expanda seu vocabulário com palavras essenciais para conversas cotidianas.',
            'ordem': 2,
            'pontos_para_desbloquear': 30 # Exemplo, ajuste conforme necessário
        }
    )
    Tarefa.objects.get_or_create(
        modulo=mod2,
        titulo='Cores Primárias e Secundárias',
        defaults={
            'conteudo_ou_pergunta': 'Liste 3 cores primárias em inglês (ex: Red, Yellow, Blue) e 2 cores secundárias (ex: Green, Orange, Purple).',
            'pontos_ao_completar': 10,
            'ordem': 1
        }
    )
    Tarefa.objects.get_or_create(
        modulo=mod2,
        titulo='Dias da Semana',
        defaults={
            'conteudo_ou_pergunta': 'Quais são os 7 dias da semana em inglês? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday). Qual o seu dia favorito e por quê? (Tente responder em inglês!)',
            'pontos_ao_completar': 15,
            'ordem': 2
        }
    )
 
    # Módulo 3: Fundamentos da Gramática
    mod3, created = ModuloAprendizado.objects.get_or_create(
        titulo='Fundamentos da Gramática',
        defaults={
            'slug': slugify('Fundamentos da Gramática'),
            'descricao': 'Entenda as estruturas básicas para formar frases corretas em inglês.',
            'ordem': 3,
            'pontos_para_desbloquear': 60 # Exemplo
        }
    )
    Tarefa.objects.get_or_create(
        modulo=mod3,
        titulo='Verbo "To Be" (Presente Simples)',
        defaults={
            'conteudo_ou_pergunta': "O verbo \"To Be\" (Ser/Estar) no presente:\n- I am (Eu sou/estou)\n- You are (Você é/está)\n- He/She/It is (Ele/Ela é/esta)\n- We are (Nós somos/estamos)\n- They are (Eles/Elas são/estão)\n\nComplete a frase: \"She ___ happy.\" (is/am/are)",
            'pontos_ao_completar': 20,
            'ordem': 1
        }
    )
    # Adicione mais tarefas e módulos conforme desejar...
 
# Função para reverter a migração (opcional, mas boa prática para dados)
# Se você não quiser implementar a reversão, pode deixar migrations.RunPython.noop
def unseed_data(apps, schema_editor):
    # Aqui você poderia deletar os dados criados se necessário.
    # Por simplicidade, vamos deixar um no-op (nenhuma operação).
    # Se quiser deletar:
    # CategoriaDica = apps.get_model('learning', 'CategoriaDica')
    # CategoriaDica.objects.filter(slug__in=[...]).delete()
    # E assim por diante para os outros modelos.
    pass
 
 
class Migration(migrations.Migration):
 
    dependencies = [
        # MUITO IMPORTANTE: Substitua 'XXXX_nome_da_migracao_anterior'
        # pelo nome real da sua última migração no app 'learning'
        # que criou os modelos CategoriaDica, Dica, ModuloAprendizado, Tarefa.
        # Ex: ('learning', '0001_initial'),
        ('ingles_facil', '0002_moduloaprendizado_tarefa_userprofile_and_more'),
    ]
 
    operations = [
        migrations.RunPython(seed_data, reverse_code=unseed_data),
    ]