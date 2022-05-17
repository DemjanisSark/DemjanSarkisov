from django.shortcuts import render
from rest_framework import generics
from .models import FacultyModel, StudentsModel, \
    BursaModel, RoomModel, ConnectionBursaRoomModel
from .serializers import FacultyModelSerializer, StudentsModelSerializer, \
    BursaModelSerializer, RoomModelSerializer, ConnectionBursaRoomModelSerializer


class FacultyView(generics.ListAPIView):
    """Представление для получения детальной информации об факультетах"""
    serializer_class = FacultyModelSerializer
    queryset = FacultyModel.objects.all()


class StudentsView(generics.ListAPIView):
    """Представление для получения детальной информации об студентах"""
    serializer_class = StudentsModelSerializer
    queryset = StudentsModel.objects.all()


class BursaView(generics.ListAPIView):
    """Представление для получения детальной информации об общежитиях"""
    serializer_class = BursaModelSerializer
    queryset = BursaModel.objects.all()


class RoomView(generics.ListAPIView):
    """Представление для получения детальной информации об комнат"""
    serializer_class = RoomModelSerializer
    queryset = RoomModel.objects.all()


class ConnectionBursaRoomView(generics.ListAPIView):
    """Представление для получения детальной информации о связях общежитий и комнат"""
    serializer_class = ConnectionBursaRoomModelSerializer
    queryset = ConnectionBursaRoomModel.objects.all()


def main_page(request):
    return render(request, "main.html")
