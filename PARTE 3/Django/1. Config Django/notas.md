# Configurando o Django

Este guia explica como criar um projeto Django básico, adicionar um app e executar a aplicação localmente.

- Link do meu projeto no Github:
  https://github.com/Guilherme-ruy/Django-Personal-Blog

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

- **Python 3.x**
- **pip** (gerenciador de pacotes Python)
- **Virtualenv** (opcional, mas recomendado)

---

## 1. Criando um Ambiente Virtual (Opcional, mas Recomendado)

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde deseja criar seu projeto.
3. Crie um ambiente virtual:
   ```bash
   python -m venv env
   ```
4. Ative o ambiente virtual:
   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **Linux/macOS**:
     ```bash
     source env/bin/activate
     ```

---

## 2. Instalando o Django

Instale o Django no ambiente virtual:

```bash
pip install django
```

Verifique se o Django foi instalado corretamente:

```bash
django-admin --version
```

---

## 3. Inicializando o Projeto Django

1. Crie um novo projeto:

   ```bash
   django-admin startproject meu_projeto
   ```

   Isso criará uma estrutura de diretórios semelhante a:

   ```
   meu_projeto/
       manage.py
       meu_projeto/
           __init__.py
           settings.py
           urls.py
           asgi.py
           wsgi.py
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd meu_projeto
   ```

---

## 4. Criando um App

1. Crie um novo app:

   ```bash
   python manage.py startapp meu_app
   ```

   Isso criará um diretório chamado `meu_app` com a seguinte estrutura:

   ```
   meu_app/
       migrations/
           __init__.py
       __init__.py
       admin.py
       apps.py
       models.py
       tests.py
       views.py
   ```

2. Registre o app no projeto. Edite o arquivo `settings.py` do diretório do projeto e adicione o nome do app à lista `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
       # Apps padrão do Django...
       'meu_app',
   ]
   ```

---

## 5. Executando a Aplicação

1. Aplique as migrações iniciais do banco de dados:

   ```bash
   python manage.py migrate
   ```

2. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

3. Abra um navegador e acesse [http://127.0.0.1:8000] ou localhost:8000 para visualizar o projeto Django em execução.

---

## Conclusão

Você agora tem um projeto Django básico com um app configurado e em execução. A partir daqui, você pode começar a desenvolver suas funcionalidades adicionando rotas, modelos e templates ao seu app.
