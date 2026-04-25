# Projeto PI

Repositório da disciplina Projeto Integrador (PI) UNIVESP.

## Descrição

Este projeto é uma aplicação completa desenvolvida principalmente em Python, integrando backend, frontend e persistência de dados. O objetivo do sistema é [DESCREVA O OBJETIVO DO SEU PROJETO, ex: gerenciar tarefas, centralizar informações acadêmicas etc.].

A aplicação possui:

- **Backend em Python**
- **Frontend com HTML/CSS e JavaScript**
- **Persistência de dados [escolha: por arquivos, SQLite, outro banco?]**
- Scripts de automação para facilitar setup
- Estrutura modular para fácil manutenção

## Estrutura do Projeto

```
.
├── pasta_backend/      # Código do backend (Python)
├── pasta_frontend/     # Arquivos HTML, CSS, JS
├── requirements.txt    # Dependências Python
├── README.md           # Este manual
└── ...                 # Outros arquivos/scripts
```

## Como rodar localmente

### Pré-requisitos

- Python 3.x instalado
- (Opcional) Virtualenv para ambiente isolado

### Passos

1. **Clone o repositório**
   ```sh
   git clone https://github.com/klitra/univesp-pi.git
   cd univesp-pi
   ```

2. **Crie e ative um ambiente virtual**
   ```sh
   python -m venv .venv
   # No Linux/Mac:
   source .venv/bin/activate
   # No Windows:
   .venv\Scripts\activate
   ```

3. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente (se necessário)**
   - Crie um arquivo `.env` e adicione as variáveis conforme o exemplo (verifique se existe `.env.example`).

5. **Inicialize o banco de dados**
   ```
   # Exemplo para Flask ou Django:
   flask db upgrade
   # ou
   python manage.py migrate
   # caso use SQLite e o banco seja criado automaticamente, pule este passo
   ```

6. **Rode o projeto**
   ```sh
   python app.py
   # ou
   flask run
   # ou
   python manage.py runserver
   ```

7. **Acesse no navegador**
   - Abra `http://localhost:5000`, `http://127.0.0.1:8000` ou porta informada no terminal.

---

## Funcionalidades

- [ ] Cadastro/Login de usuários
- [ ] CRUD de entidades principais
- [ ] Interface web
- [ ] Integração com banco de dados
- [ ] [Outras funções específicas do seu projeto]

## Contribuição

Sinta-se livre para abrir issues ou pull requests. Sugestões são bem-vindas!

---

> _Ajuste nomes de arquivos, comandos e frameworks conforme seu projeto de fato._


Integrantes

Carlos Eduardo Sousa Rodrigues, 2206894  
Aldalis Ferreira França Gomes, 23207804  
Carlos Gomes de Oliveira, 2108356  
Marcelo Yoshio Yasuoka Sasahara, 23220281  
Kleber Gonçalves, 2101919  
Marco Aurélio Santos de Moura, 2224178  
Julio Cesar Ribeiro Duarte, 23218534  
Karen Lais Novais Cruz - 23202803



