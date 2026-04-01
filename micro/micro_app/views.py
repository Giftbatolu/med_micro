from django.shortcuts import render
from rest_framework import generics
from .models import Microoganism
from .serializers import MicroSerializer

class MicroListCreateView(generics.ListCreateAPIView):
    queryset = Microoganism.objects.all()
    serializer_class = MicroSerializer