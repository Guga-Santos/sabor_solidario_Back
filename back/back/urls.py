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
from voluntarios.api.routes import VoluntariosRoutes
from campanha.api.routes import CampanhasRoutes
from transacao import views as transacao

route = routers.DefaultRouter()
route.register('transacoes', transacoes.TransacaoViewSet, basename='Transacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurantes/', include(RestauranteRoutes())),
    path('voluntarios/', include(VoluntariosRoutes())),
    path('campanhas/', include(CampanhasRoutes())),
    path('transacoes/', transacao.Overview),
    path('transacoes/list/<str:pk>', transacao.Find_By_Id),
    path('transacoes/list/', transacao.List),
    path('transacoes/create/', transacao.Create),
    path('transacoes/update/<str:pk>', transacao.Update),
    path('transacoes/delete/<str:pk>', transacao.Delete),
    path('', include(route.urls)),
]
