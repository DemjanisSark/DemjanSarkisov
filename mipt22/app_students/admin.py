from django.contrib import admin
from .models import StudentsModel, BursaModel, ConnectionBursaRoomModel, RoomModel, FacultyModel


class StudentInLine(admin.TabularInline):
    model = StudentsModel


class ConnectionBursaRoomInLine(admin.TabularInline):
    model = ConnectionBursaRoomModel


@admin.register(StudentsModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", 'full_name', 'course']


@admin.register(BursaModel)
class BursaAdmin(admin.ModelAdmin):
    list_display = ["id", 'address', 'description']
    inlines = [ConnectionBursaRoomInLine]


@admin.register(ConnectionBursaRoomModel)
class ConnectionBursaRoomAdmin(admin.ModelAdmin):
    list_display = ["id", 'bursa', 'room']


@admin.register(RoomModel)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["id", 'number']
    inlines = [ConnectionBursaRoomInLine]


@admin.register(FacultyModel)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ["id", 'specialization']
    inlines = [StudentInLine]





