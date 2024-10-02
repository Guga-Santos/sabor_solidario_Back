from django.urls import path
from transacao import views as transacao

def TransacoesRoutes():
    routes = [
        path('', transacao.Overview),
        path('list/<str:pk>', transacao.Find_By_Id),
        path('list/', transacao.List),
        path('create/', transacao.Create),
        path('update/<str:pk>', transacao.Update),
        path('delete/<str:pk>', transacao.Delete),
    ]
    return routes