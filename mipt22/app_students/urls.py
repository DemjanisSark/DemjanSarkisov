from django.urls import path
from .views import FacultyView, StudentsView,\
    BursaView, RoomView, ConnectionBursaRoomView, main_page

urlpatterns = [
    path('faculty', FacultyView.as_view()),
    path('students', StudentsView.as_view()),
    path('bursa', BursaView.as_view()),
    path('room', RoomView.as_view()),
    path('connection', ConnectionBursaRoomView.as_view()),
    path('', main_page)
]
