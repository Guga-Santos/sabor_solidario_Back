from django.urls import path
from restaurantes import views as restaurante

def RestauranteRoutes():
    routes = [
        path('', restaurante.Overview),
        path('list/<str:pk>', restaurante.Find_By_Id),
        path('list/', restaurante.List),
        path('create/', restaurante.Create),
        path('update/<str:pk>', restaurante.Update),
        path('delete/<str:pk>', restaurante.Delete),
    ]
    return routes