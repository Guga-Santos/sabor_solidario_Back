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
                "find_by_id":"http://127.0.0.1:8000/transacoes/list/<str:pk>",
                "create":"http://127.0.0.1:8000/transacoes/create",
                "update":"http://127.0.0.1:8000/transacoes/update",
                "delete":"http://127.0.0.1:8000/transacoes/delete"
            },
            "Campanhas": {
                "list":"http://127.0.0.1:8000/campanhas/list",
                "find_by_id":"http://127.0.0.1:8000/campanhas/list/<str:pk>",
                "create":"http://127.0.0.1:8000/campanhas/create",
                "update":"http://127.0.0.1:8000/campanhas/update",
                "delete":"http://127.0.0.1:8000/campanhas/delete"
            },
            "Restaurantes": {
                "list":"http://127.0.0.1:8000/restaurantes/list",
                "find_by_id":"http://127.0.0.1:8000/restaurantes/list/<str:pk>",
                "create":"http://127.0.0.1:8000/restaurantes/create",
                "update":"http://127.0.0.1:8000/restaurantes/update",
                "delete":"http://127.0.0.1:8000/restaurantes/delete"
            },
            "Voluntários": {
                "list":"http://127.0.0.1:8000/voluntarios/list",
                "find_by_id":"http://127.0.0.1:8000/voluntarios/list/<str:pk>",
                "create":"http://127.0.0.1:8000/voluntarios/create",
                "update":"http://127.0.0.1:8000/voluntarios/update",
                "delete":"http://127.0.0.1:8000/voluntarios/delete"
            }
        }
        return Response(message, status=status.HTTP_200_OK)
