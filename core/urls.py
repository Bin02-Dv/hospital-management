from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signUp', views.signUp, name='signUp'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('patient-view', views.patient_view, name='patient-view'),
    path('room-list', views.room_list, name='room-list'),
    path('add-patient', views.add_patient, name='add-patient'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('p-details/<int:pk>', views.p_details, name='p-details'),
    path('search', views.search, name='search')
]