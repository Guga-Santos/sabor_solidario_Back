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
from transacao.api import viewsets as transacoes

from restaurantes.api.routes import RestauranteRoutes
from voluntarios import views as voluntario
from campanha import views as campanha
from transacao import views as transacao

route = routers.DefaultRouter()
route.register('transacoes', transacoes.TransacaoViewSet, basename='Transacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurantes/', include(RestauranteRoutes())),
    path('voluntarios/', voluntario.Overview),
    path('voluntarios/list/<str:pk>', voluntario.Find_By_Id),
    path('voluntarios/list/', voluntario.List),
    path('voluntarios/create/', voluntario.Create),
    path('voluntarios/update/<str:pk>', voluntario.Update),
    path('voluntarios/delete/<str:pk>', voluntario.Delete),
    path('campanhas/', campanha.Overview),
    path('campanhas/list/<str:pk>', campanha.Find_By_Id),
    path('campanhas/list/', campanha.List),
    path('campanhas/create/', campanha.Create),
    path('campanhas/update/<str:pk>', campanha.Update),
    path('campanhas/delete/<str:pk>', campanha.Delete),
    path('transacoes/', transacao.Overview),
    path('transacoes/list/<str:pk>', transacao.Find_By_Id),
    path('transacoes/list/', transacao.List),
    path('transacoes/create/', transacao.Create),
    path('transacoes/update/<str:pk>', transacao.Update),
    path('transacoes/delete/<str:pk>', transacao.Delete),
    path('', include(route.urls)),
]
