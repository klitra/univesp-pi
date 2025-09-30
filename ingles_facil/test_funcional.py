# Em: ingles_facil/test_pagina_inicial.py

import pytest
from playwright.sync_api import Page, expect
import re

# Garante que o banco de dados de teste do Django seja criado
@pytest.mark.django_db
def test_pagina_inicial_carrega_corretamente(page: Page, live_server):
    """
    Um teste simples para verificar se a página inicial carrega
    e exibe o título e o cabeçalho principal corretamente.
    """
    
    # 1. Navega para a página inicial do site de teste
    page.goto(live_server.url)

    # 2. Verifica se o título da aba do navegador está correto.
    #    Isso confirma que o template base foi carregado.
    expect(page).to_have_title(re.compile("Página Inicial|Vivo Idiomas"))

    # 3. Verifica se o cabeçalho principal da página está visível.
    #    Isso confirma que o conteúdo específico da home page foi renderizado.
    #    (Ajustado com base na imagem do seu site que você enviou antes)
    expect(page.get_by_role("heading", name="Explore por Categoria")).to_be_visible()

    # 4. Verifica se o link de "Cadastro" existe na página.
    #    Isso confirma que a navegação para o próximo passo está disponível.
    expect(page.get_by_text("Cadastro")).to_be_visible()