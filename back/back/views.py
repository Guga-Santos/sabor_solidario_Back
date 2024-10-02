# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ApiRootView(APIView):
    def get(self, request, *args, **kwargs):
        # Mensagem personalizada com rotas disponíveis
        message = {
            "message": "Bem-vindo à API Sabor Solidário!",
            "api": "http://127.0.0.1:8000/api/",
            "Transações": {
                "list":"http://127.0.0.1:8000/transacoes/list",
                "create":"http://127.0.0.1:8000/transacoes/create",
                "find_by_id":"http://127.0.0.1:8000/transacoes/list/<str:pk>",
                "update":"http://127.0.0.1:8000/transacoes/update/<str:pk>",
                "delete":"http://127.0.0.1:8000/transacoes/delete/<str:pk>"
            },
            "Campanhas": {
                "list":"http://127.0.0.1:8000/campanhas/list",
                "create":"http://127.0.0.1:8000/campanhas/create",
                "find_by_id":"http://127.0.0.1:8000/campanhas/list/<str:pk>",
                "update":"http://127.0.0.1:8000/campanhas/update/<str:pk>",
                "delete":"http://127.0.0.1:8000/campanhas/delete/<str:pk>"
            },
            "Restaurantes": {
                "list":"http://127.0.0.1:8000/restaurantes/list",
                "create":"http://127.0.0.1:8000/restaurantes/create",
                "find_by_id":"http://127.0.0.1:8000/restaurantes/list/<str:pk>",
                "update":"http://127.0.0.1:8000/restaurantes/update/<str:pk>",
                "delete":"http://127.0.0.1:8000/restaurantes/delete/<str:pk>"
            },
            "Voluntários": {
                "list":"http://127.0.0.1:8000/voluntarios/list",
                "create":"http://127.0.0.1:8000/voluntarios/create",
                "find_by_id":"http://127.0.0.1:8000/voluntarios/list/<str:pk>",
                "update":"http://127.0.0.1:8000/voluntarios/update/<str:pk>",
                "delete":"http://127.0.0.1:8000/voluntarios/delete/<str:pk>"
            }
        }
        return Response(message, status=status.HTTP_200_OK)
