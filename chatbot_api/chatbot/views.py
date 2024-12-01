from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Chatbot
from .serializers import ChatbotSerializer

class ChatbotViewSet(viewsets.ModelViewSet):
    queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer
