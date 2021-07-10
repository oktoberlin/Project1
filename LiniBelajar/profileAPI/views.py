from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProfileSerializer

from user.models import Profile
# Create your views here.


class ProfileCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Profile.objects.all(),
    serializer_class = ProfileSerializer


class ProfileList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer