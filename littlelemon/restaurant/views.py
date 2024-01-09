from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions, viewsets
from . import serializers
from .models import Menu, Booking

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset= Booking.objects.all()
    serializer_class= serializers.BookingSerializer
    permission_classes= [permissions.IsAuthenticated]