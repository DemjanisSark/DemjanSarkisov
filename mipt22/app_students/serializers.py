from .models import FacultyModel, StudentsModel, BursaModel, RoomModel, ConnectionBursaRoomModel
from rest_framework import serializers


class FacultyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyModel
        fields = ['specialization']


class StudentsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsModel
        fields = ['full_name', 'course', 'faculty']


class BursaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BursaModel
        fields = ['address', 'description']


class RoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomModel
        fields = ['number', 'students']


class ConnectionBursaRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionBursaRoomModel
        fields = ['bursa', 'room']
