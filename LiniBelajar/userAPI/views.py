from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer

from django.contrib.auth.models import User
# Create your views here.


class UserCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = User.objects.all(),
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = User.objects.all()
    serializer_class = UserSerializer
