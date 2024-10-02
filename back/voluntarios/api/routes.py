from django.urls import path
from voluntarios import views as voluntario

def VoluntariosRoutes():
    routes = [
        path('', voluntario.Overview),
        path('list/<str:pk>', voluntario.Find_By_Id),
        path('list/', voluntario.List),
        path('create/', voluntario.Create),
        path('update/<str:pk>', voluntario.Update),
        path('delete/<str:pk>', voluntario.Delete),
    ]
    return routes