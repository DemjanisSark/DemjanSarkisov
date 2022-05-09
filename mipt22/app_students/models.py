from django.db import models


class FacultyModel(models.Model):
    specialization = models.CharField(max_length=30, verbose_name='Специальность')


class StudentsModel(models.Model):
    full_name = models.CharField(max_length=99, editable=True, default=None, verbose_name='ФИО')
    course = models.IntegerField(editable=True, default=None, verbose_name='Курс')
    faculty = models.ForeignKey(FacultyModel, on_delete=models.CASCADE, verbose_name='Специальность')


class BursaModel(models.Model):
    address = models.CharField(max_length=99, editable=True, default=None, verbose_name='Адрес')
    description = models.CharField(max_length=200, editable=True, default=None, verbose_name='Описание')


class RoomModel(models.Model):
    number = models.CharField(max_length=10, editable=True, default=None, verbose_name='Номер Комнаты')
    students = models.ManyToManyField(StudentsModel, verbose_name='')


class ConnectionBursaRoomModel(models.Model):
    bursa = models.ForeignKey(BursaModel, on_delete=models.CASCADE, verbose_name='Id общежития')
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, verbose_name='Id общежития')