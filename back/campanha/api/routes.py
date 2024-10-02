from django.urls import path
from campanha import views as campanha

def CampanhasRoutes():
    routes = [
        path('', campanha.Overview),
        path('list/<str:pk>', campanha.Find_By_Id),
        path('list/', campanha.List),
        path('create/', campanha.Create),
        path('update/<str:pk>', campanha.Update),
        path('delete/<str:pk>', campanha.Delete),
    ]
    return routes