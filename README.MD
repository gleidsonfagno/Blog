# PROJETO CARROS

Criando ambiente virtual e ativando o abiente virtual e intalando o django

- ``python -m venv venv``
- ``.\venv\Scripts\activate``
- ``pip install django``
- ``django-admin --version``

Criando projeto Django

- django-admin startproject app .
  - [x] Vai criar as estrutura de pasta
  - [x] O app e o nome do projeto e o "." e para criar no msmodiretorio onde estamos
- python manage.py runserver
  - [x] Vai startar um servidor que javem embutido de desenvolvimento para testar por padrao na porta 8.000

## apps no python

Criando a app em python

- ``python manage.py startapp cars``

```meuapp/
├── migrations/
│   ├── __init__.py
├── admin.py 
├── apps.py 
├── models.py 
├── tests.py 
└── views.py 
```

```python
# Adicionar em settings.py
INSTALLED_APPS = [
  "cars",
  # senao ele nao vai entender
]
```

## Entendendo Apps e Camadas no Django

- migrations/: Armazena migrações de banco de dados para o aplicativo.
- admin.py: Configurações relacionadas à administração do aplicativo.
- apps.py: Configurações específicas do aplicativo, como nome legível por humanos.
- models.py: Define os modelos de dados do aplicativo.
- tests.py: Contém testes unitários para o aplicativo.
- views.py: Define as funções de visualização do aplicativo.

## Comando makemigrations e Comando migrate

Os comandos makemigrations e migrate são fundamentais no Django para gerenciar mudanças no esquema do banco de dados com base nas alterações feitas nos modelos (models).

- python manage.py makemigrations
- python manage.py migrate
  
## Acessando o Admin do Django

- python manage.py createsuperuser

```bash
Username (leave blank to use 'empreendedor'): gledson
Email address: gleidson@gmail.com
Password: 123
Password (again): 
```

## Criando nosso primeiro modelo (News)

No arquivo model.py cria o banco de dados e depois da o comando makemigrations e o migrate ele atarve do orm do django e traduz para sql e cria o banco de dados.

## Configurando o Admin do nosso model (News)

No arquivo admin.py ele que e responsalvel pela adminstracao
e adiciona os campos nessesario.

## Configurações adicionais do nosso projeto

```python
def __str__(self):
    return self.model
```

Esse método está retornando o valor do atributo model do objeto. Isso significa que, quando você imprimir uma instância dessa classe, o valor de model será exibido.

## Criando modelo e admin de marcas (ForeignKey)

```py
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
```

vamos criar uma nova tabela dde dados e ela vai esta relacionado com a tabela de car
brand (ForeignKey): Referência à classe Brand. Define a marca do carro.
on_delete=models.PROTECT: Impede a exclusão de uma marca se houver carros associados a ela.

## Armazenando imagens dos carros

Para usar esses campo de imagen tem que instalar essa bibioteca

``python -m pip install Pillow``

depois coloca o campo de imagem
``photo = models.ImageField(upload_to="news/", blank=True, null=True)``
adiciona essas configuracoes no settings.py

```python
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
```

depois colca essa no urls.py e com as importacoes

```python
# para a configuracoo de upload de imagens
from django.conf import settings
from django.conf.urls.static import static

# quando e pessoal escrever /admin na url vai renderizar 
urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # para a configuracoo de upload de imagens
```

## Visão de admin VS visão de usuário

## Entendendo URLs e Views

Cria a funça dentro da views e e imparta a url no arquivo urls.py para funcionar as rotas

```python
# urls.py
# na url vai chamr a funcao que esta nela
from cars.views import cars_view

# views.py
# http para as rotas
from django.http import HttpResponse
# Create your views here.

def cars_view(request):
    return HttpResponse("Meus carros 1")
```

## URLs, Views e Templates Entendendo Templates

## Retornando Templates para o usuário

Crimaos uma pasta chamada templates/cars.html.
O python ja etende que la tem alguma coisa

```python
from django.shortcuts import render

def cars_view(request):
    # ela renderiza o http do html e devolve uma response para o usuario
    return render(request, 'cars.html')
```

## Linguagem de Templates do Django

esse metodo de linguagem e para acessar os dados do banco de dados 

```html
{% block content %}
<body>
    <h1>Carros do gleidso fagno</h1>
    <h3>{{cars.model}}</h3>
</body>
{% endblock %}
```
