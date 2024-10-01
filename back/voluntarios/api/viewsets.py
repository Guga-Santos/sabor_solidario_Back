from rest_framework import viewsets
from voluntarios.api import serializers
from voluntarios import models

class VoluntariosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VoluntariosSerializer
    queryset = models.Voluntarios.objects.all()