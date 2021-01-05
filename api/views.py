from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Room
from django.shortcuts import render
from rest_framework import generics, status
from.serializers import RoomSerializer
# Create your views here.


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
