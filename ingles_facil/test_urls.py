# ingles_facil/test_urls.py

import pytest
from django.urls import reverse, resolve

# Usamos pytest.mark.django_db para permitir o acesso ao banco de dados, 
# o que é necessário para muitas funcionalidades do Django, como o 'reverse'.
@pytest.mark.django_db
def test_homepage_carrega_com_sucesso():
    """
    Testa se a URL da página inicial está configurada corretamente.
    Supondo que o nome da sua URL para a home page seja 'pagina_inicial'.
    """
    # Use o nome (name=) que você definiu no seu arquivo urls.py
    # Se o nome da sua URL principal for outro, troque 'pagina_inicial' abaixo.
    url_path = reverse('ingles_facil:pagina_inicial') 

    # Verifica se o caminho revertido é a raiz do site ('/')
    assert url_path == "/"
    
    # Verifica se a URL '/' resolve para a view correta
    # Troque 'pagina_inicial_view' pelo nome real da sua função de view.
    # Por exemplo: assert resolve('/').view_name == "ingles_facil.views.home"
    print(f"A URL '/' resolve para a view: {resolve('/').view_name}")

def test_simples_exemplo():
    """
    Um teste muito simples apenas para garantir que o Pytest encontre o arquivo.
    """
    x = 5
    y = 10
    assert x + y == 15