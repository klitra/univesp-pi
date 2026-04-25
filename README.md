# Projeto PI – Owlstip

Repositório do Projeto Integrador UNIVESP – Owlstip: sua plataforma web para alavancar o aprendizado de inglês de forma gamificada, moderna e acessível.

## Visão Geral

Este projeto é uma aplicação web completa criada com Django, projetada para ser fácil de usar, acessível e escalável. O objetivo é disponibilizar um ambiente virtual de estudo de inglês, com:

- sistema de dicas organizadas por categoria (apps, músicas, séries, etc.);
- módulos de aprendizado e trilhas com tarefas;
- progresso e gamificação (pontos, fases/crescimento de perfil do usuário);
- interface web interativa, responsiva e amigável.

A solução cobre backend, frontend, banco de dados, autenticação, painel de administração, controle de progresso, experiência gamificada e está pronta para deploy em nuvem (compatibilidade especial com Render).

## Principais Funcionalidades

- **Cadastro e Login de Usuários**: Controle de acessos seguro (usuário padrão do Django + perfis estendidos).
- **Gamificação**: Perfil do usuário com conquistas, pontos e etapas de crescimento.
- **Módulos e Tarefas de Aprendizagem**: Organização em trilhas progressivas; cada módulo com tarefas interativas.
- **Sistema de Dicas**: Dicas categorizadas (ex: aplicativos, músicas, séries) com descrição detalhada, links e logos.
- **Banco de Dados Integrado**: Pronto para SQLite (desenvolvimento) e PostgreSQL (produção/Render).
- **Administração Completa**: Painel Django Admin para gestão de usuários, dicas, progresso, etc.
- **Frontend Customizado**: Templates HTML, CSS moderno, responsivo, navegação amigável e layout visualmente atraente.
- **Implantação Facilitada**: Compatível com Render, uso de Gunicorn e Whitenoise para produção e arquivos estáticos, variáveis de ambiente via .env.

---

## Estrutura do Projeto (resumida)

```
/
├── manage.py
├── requirements.txt
├── vivoidiomas/                  # Configurações e root do projeto Django
│   ├── settings.py, urls.py, ...
├── ingles_facil/                 # App principal: regras de negócio
│   ├── models.py, views.py, ...
├── templates/                    # HTML (base, páginas, etc.)
├── static/                       # CSS, imgs, JS
├── .env.example                  # Exemplo de configuração ambiente
├── db.sqlite3                    # (Auto) Para rodar localmente
```

---

## Como Rodar Localmente

### 1. Clonar o repositório
```sh
git clone https://github.com/klitra/univesp-pi.git
cd univesp-pi
```

### 2. Criar ambiente virtual
```sh
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate
```

### 3. Instalar dependências
```sh
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto (baseie-se no `.env.example`, ou configure pelo menos as variáveis essenciais, como SECRET_KEY):

```
SECRET_KEY=suasupersecret
DEBUG=True
```
*(na produção, defina DEBUG=False e configure o banco PostgreSQL; ambiente local funciona com o SQLite já configurado.)*

### 5. Executar migrações e preparar banco
```sh
python manage.py migrate
```

### 6. (Opcional) Criar superusuário para acessar o admin
```sh
python manage.py createsuperuser
```

### 7. Rodar o servidor de desenvolvimento
```sh
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

---

## Deploy em Produção

- Para produção (exemplo: Render), configure variáveis de ambiente: ajuste `DEBUG`, chaves, banco PostgreSQL, e execute os comandos de collectstatic para arquivos estáticos:
  ```sh
  python manage.py collectstatic
  ```

- O projeto já inclui Gunicorn e Whitenoise para servir arquivos estáticos corretamente em ambiente de produção.

---

## Créditos, Licença e Colaboradores

Este projeto é de uso acadêmico, mas pode servir como base para aplicativos de ensino/aprendizado de idiomas. Fique à vontade para abrir issues, sugerir melhorias ou enviar pull requests!

> **Equipe:** jduarte95 e colaboradores UNIVESP <!-- (alterar/expandir conforme necessário) -->

---


## Exemplos de Recursos

### Perfis do Usuário
Os usuários avançam de "Novato Curioso" até "Mestre do Idioma", acumulando pontos ao completar tarefas.

### Trilhas e Módulos
Cada trilha libera módulos progressivos, incentivando o estudo contínuo e focado.

### Dicas Interativas
Dicas personalizadas para apps, vídeos, músicas, sites e outros recursos, tudo categorizado e com link útil.

---

## FAQ Rápido

- **Qual o banco local?** Por padrão é SQLite (`db.sqlite3` já pronto após as migrações).
- **Posso usar PostgreSQL?** Sim, basta alterar o `DATABASES` no `.env` ou overriding via settings.
- **Suporta deploy em nuvem?** Sim, pronto para Render.com, Heroku, Azure, etc.

---
