from django.db import models

class CategoriaDica(models.Model):
    nome = models.CharField(max_length=100, unique=True, help_text="Ex: Aplicativos, Músicas, Séries")
    slug = models.SlugField(max_length=100, unique=True, help_text="URL amigável (letras minúsculas, números, hífens)")
    descricao_breve = models.TextField(blank=True, null=True, help_text="Pequena descrição da categoria")
    cor_card = models.CharField(max_length=7, default="#660099", help_text="Cor em hexadecimal (ex: #660099)")

    def __str__(self): # Define como o objeto será exibido (ex: no admin)
        return self.nome

    class Meta: # Metadados do modelo
        verbose_name = "Categoria de Dica"
        verbose_name_plural = "Categorias de Dicas"
        ordering = ['nome'] # Ordenar por nome por padrão

class Dica(models.Model):
    categoria = models.ForeignKey(CategoriaDica, on_delete=models.CASCADE, related_name="dicas") # Relação com CategoriaDica
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField(help_text="A dica detalhada.")
    link_util = models.URLField(blank=True, null=True, help_text="Link externo relevante, se houver.")
    data_adicionada = models.DateTimeField(auto_now_add=True) # Data e hora de criação automática
    nome_recurso = models.CharField(max_length=100, blank=True, null=True, help_text="Nome do site ou app. Ex: Duolingo")
    logo_recurso = models.ImageField(upload_to='midia/logos_recursos/', blank=True, null=True, help_text="Logo do site ou app.")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Dica"
        verbose_name_plural = "Dicas"
        ordering = ['-data_adicionada'] # Dicas mais recentes primeiro

from django.contrib.auth.models import User # Modelo de usuário padrão do Django
from django.db.models.signals import post_save # Para executar ações após salvar um modelo
from django.dispatch import receiver # Para receber o sinal

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile") # Relação um-para-um com User
    pontos_totais = models.PositiveIntegerField(default=0)
    # foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True) # Exemplo

    def __str__(self):
        return self.user.username

    def get_etapa_crescimento(self):
        if self.pontos_totais < 50:
            return "Novato Curioso"
        elif self.pontos_totais < 150:
            return "Explorador de Palavras"
        elif self.pontos_totais < 300:
            return "Aprendiz Dedicado"
        elif self.pontos_totais < 500:
            return "Conquistador de Frases"
        else:
            return "Mestre do Idioma"

# Sinal para criar/atualizar UserProfile automaticamente quando um User é criado/salvo
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created: # Se um novo usuário foi criado
        UserProfile.objects.create(user=instance)
    # Se o perfil já existe, apenas salva. Pode ser útil se houver lógica no save do perfil.
    # No caso de UserProfile simples, instance.profile.save() pode não ser sempre necessário aqui
    # se não houver atualizações no perfil disparadas por salvar o User, além da criação.
    # Mas é seguro manter para garantir consistência.
    try:
        instance.profile.save()
    except UserProfile.DoesNotExist: # Caso o perfil não tenha sido criado por algum motivo raro
        UserProfile.objects.create(user=instance)


class ModuloAprendizado(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    descricao = models.TextField(blank=True)
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem de apresentação dos módulos")
    # icone = models.ImageField(upload_to='icones_modulos/', blank=True, null=True) # Se quiser ícones
    pontos_para_desbloquear = models.PositiveIntegerField(default=0, help_text="Pontos totais necessários para acessar este módulo")

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['ordem']
        verbose_name = "Módulo de Aprendizado"
        verbose_name_plural = "Módulos de Aprendizado"
class Tarefa(models.Model):
    modulo = models.ForeignKey(ModuloAprendizado, on_delete=models.CASCADE, related_name="tarefas")
    titulo = models.CharField(max_length=200)
    # TIPO_TAREFA_CHOICES = [('multipla_escolha', 'Múltipla Escolha'), ('video', 'Vídeo Aula'), ('leitura', 'Leitura')]
    # tipo = models.CharField(max_length=50, choices=TIPO_TAREFA_CHOICES, default='leitura')
    conteudo_ou_pergunta = models.TextField(help_text="Descrição da tarefa, texto para leitura, pergunta do quiz, link do vídeo, etc.")
    # resposta_correta = models.CharField(max_length=255, blank=True, help_text="Para tarefas com resposta única, se aplicável")
    pontos_ao_completar = models.PositiveIntegerField(default=10)
    ordem = models.PositiveIntegerField(default=0, help_text="Ordem da tarefa dentro do módulo")

    def __str__(self):
        return f"{self.modulo.titulo} - {self.titulo}"

    class Meta:
        ordering = ['modulo__ordem', 'ordem'] # Ordena primeiro pela ordem do módulo, depois pela ordem da tarefa
        verbose_name = "Tarefa de Aprendizado"
        verbose_name_plural = "Tarefas de Aprendizado"

class ProgressoUsuarioTarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="progresso_tarefas")
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
    completada = models.BooleanField(default=False)
    data_conclusao = models.DateTimeField(null=True, blank=True) # Data/hora da conclusão

    class Meta:
        unique_together = ('usuario', 'tarefa') # Garante que um usuário só tenha um registro de progresso por tarefa
        verbose_name = "Progresso do Usuário na Tarefa"
        verbose_name_plural = "Progressos dos Usuários nas Tarefas"

    def __str__(self):
        return f"{self.usuario.username} - {self.tarefa.titulo} ({'OK' if self.completada else 'Pendente'})"
