from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restaurantes.models import Restaurantes
from restaurantes.api.serializers import RestaurantesSerializers

# Create your views here.


