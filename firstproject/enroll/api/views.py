from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Studentserializer
from enroll.models import Data
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class Firstview(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = Studentserializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]