# Django Auth Boilerplate 🚀

Este é um projeto base em Django com sistema de autenticação completo.

## Funcionalidades
- [x] Login / Logout
- [x] Registro de novos usuários
- [x] Recuperação de senha (Reset via terminal no console)
- [x] Limpeza automática de tokens sujos (correção do `=` do terminal)

## Como usar
1. Clone o repositório
2. Crie o venv: `python -m venv .venv`
3. Ative o venv: `.\.venv\Scripts\Activate.ps1`
4. Instale as dependências: `pip install -r requirements.txt`
5. Rode as migrations: `python manage.py migrate`
6. Inicie: `python manage.py runserver`

## Dica do Reset de Senha
Ao testar o reset no ambiente de desenvolvimento, o link aparecerá no terminal. 
O projeto já conta com uma View personalizada para limpar automaticamente caracteres 
inválidos gerados pela quebra de linha do console. Mas é sempre bom lembrar que ao copiar do terminal, caracteres "invisiveis" também são copiados para o navegador, gerando uma quebra do token final.

## Configure o seu e-mail, smtp, host, e-mail e password
Ao testar este projeto, configure o seu user, mas configure seu e-mail, host e demais coisas. É importante que seja possível construir um projeto vinculado ao seu e-mail. Não adianta baixar este projeto e não configurar as suas especificidades pessoais, fique atento.

