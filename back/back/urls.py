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
from voluntarios.api import viewsets as voluntarios
from campanha.api import viewsets as campanhas
from transacao.api import viewsets as transacoes

from restaurantes import views as restaurante
from voluntarios import views as voluntario

route = routers.DefaultRouter()
route.register('campanhas', campanhas.CampanhaViewSet, basename='Campanhas')
route.register('transacoes', transacoes.TransacaoViewSet, basename='Transacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurantes/', restaurante.Overview),
    path('restaurantes/list/<str:pk>', restaurante.Find_By_Id),
    path('restaurantes/list/', restaurante.List),
    path('restaurantes/create/', restaurante.Create),
    path('restaurantes/update/<str:pk>', restaurante.Update),
    path('restaurantes/delete/<str:pk>', restaurante.Delete),
    path('voluntarios/', voluntario.Overview),
    path('voluntarios/list/<str:pk>', voluntario.Find_By_Id),
    path('voluntarios/list/', voluntario.List),
    path('voluntarios/create/', voluntario.Create),
    path('voluntarios/update/<str:pk>', voluntario.Update),
    path('voluntarios/delete/<str:pk>', voluntario.Delete),
    path('', include(route.urls)),
]
