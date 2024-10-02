
from django.contrib import admin
from django.urls import path, include

from .views import ApiRootView

from rest_framework import routers
from transacao.api import viewsets as transacoes
from campanha.api import viewsets as campanhas
from restaurantes.api import viewsets as restaurantes
from voluntarios.api import viewsets as voluntarios

from restaurantes.api.routes import RestauranteRoutes
from voluntarios.api.routes import VoluntariosRoutes
from campanha.api.routes import CampanhasRoutes
from transacao.api.routes import TransacoesRoutes

route = routers.DefaultRouter()
route.register('transacoes', transacoes.TransacaoViewSet, basename='Transacoes')
route.register('campanhas', campanhas.CampanhaViewSet, basename='Campanhas')
route.register('restaurantes', restaurantes.RestauranteViewSet, basename='Restaurantes')
route.register('voluntarios', voluntarios.VoluntariosViewSet, basename='Voluntarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApiRootView.as_view(), name='api-root'),
    path('restaurantes/', include(RestauranteRoutes())),
    path('voluntarios/', include(VoluntariosRoutes())),
    path('campanhas/', include(CampanhasRoutes())),
    path('transacoes/', include(TransacoesRoutes())),
    path('api/', include(route.urls)),
]
