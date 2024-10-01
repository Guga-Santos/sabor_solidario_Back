"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from restaurantes.api import viewsets as restaurantes
from voluntarios.api import viewsets as voluntarios
from campanha.api import viewsets as campanhas
from transacao.api import viewsets as transacoes

from restaurantes.views import List, Find_By_Id, Create

route = routers.DefaultRouter()

route.register('restaurantes', restaurantes.RestauranteViewSet, basename='Restaurantes')
route.register('voluntarios', voluntarios.VoluntariosViewSet, basename='Voluntarios')
route.register('campanhas', campanhas.CampanhaViewSet, basename='Campanhas')
route.register('transacoes', transacoes.TransacaoViewSet, basename='Transacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurantes/list/<str:pk>', Find_By_Id),
    path('restaurantes/list/', List),
    path('restaurantes/create/', Create),
    path('', include(route.urls)),
]
