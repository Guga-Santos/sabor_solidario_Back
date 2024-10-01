# Sabor Solidário

Este é um projeto Django para gerenciar informações sobre restaurantes e seus endereços, visando promover a solidariedade e a gastronomia local.

## Pré-requisitos

Antes de começar, verifique se você tem as seguintes ferramentas instaladas: Python 3.x, Pip, Virtualenv, Django e Django REST Framework.

## Configuração do Ambiente

Siga os passos abaixo para configurar o projeto em sua máquina local.

# **Clonar o Repositório**
   ```bash
   git clone https://github.com/seu_usuario/Sabor_Solidario.git
   cd Sabor_Solidario/BackEnd/back
   ```

# **Criar e Ativar o Ambiente Virtual**

## Instale o virtualenv se não tiver
```bash
pip install virtualenv
```

## Crie um ambiente virtual
```bash
virtualenv venv
```

## Ative o ambiente virtual
## No Windows
```bash
venv\Scripts\activate
```
## No macOS/Linux
```bash
source venv/bin/activate
```


# **Instalar as Dependências**
```bash
pip install -r requirements.txt
```

# **Configurar o Banco de Dados**
#### Edite o arquivo settings.py para configurar as credenciais do seu banco de dados. Depois, execute as migrações:
```bash
python manage.py migrate
```

# **Rodar o Servidor**
```bash
python manage.py runserver

```

## Agora você pode acessar o projeto em http://127.0.0.1:8000/.

# ** Estrutura do Projeto
### A estrutura do projeto deve se parecer com isso:

```bash
/home/caminho/ate/sua/pasta
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    ├── back/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── campanha/
    │   └── __pycache__/
    │   └── api/
    │       ├── serializers.py
    │       └── viewsets.py
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py    
    ├── restaurantes/
    │   └── __pycache__/
    │   └── api/
    │       ├── serializers.py
    │       └── viewsets.py
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── transacao/
    │   └── __pycache__/
    │   └── api/
    │       ├── serializers.py
    │       └── viewsets.py
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── voluntarios/
    │   └── __pycache__/
    │   └── api/
    │       ├── serializers.py
    │       └── viewsets.py
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
        

```


#### Este projeto está licenciado sob a Licença MIT.


