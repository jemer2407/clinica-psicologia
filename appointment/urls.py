from django.urls import path
from . import views

urlpatterns = [
    path('appointment/', views.AppointmentListView.as_view(), name='appointment-list'),
    path('appointment/create/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointment/update/<int:pk>/', views.AppointmentUpdateView.as_view(), name='appointment-update'),
    path('appointment/delete/<int:pk>/', views.AppointmentDeleteView.as_view(), name='appointment-delete'),
    path('appointment/patient/<int:pk>/', views.AppointmentPatientListView.as_view(), name='appointment-patient-list'),
]