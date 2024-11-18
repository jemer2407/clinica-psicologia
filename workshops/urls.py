from django.urls import path
from . import views

urlpatterns = [
    path('workshops/', views.WorkshopListView.as_view(), name='workshops-list'),
    path('workshops/<int:pk>/<slug:slug>/', views.WorkshopDetailView.as_view(), name='workshops-detail'),
    path('workshops/professional/<int:pk>/', views.WorkshopProfessionalListView.as_view(), name='workshops-professional-list'),
    path('workshops/specialty/<int:pk>/', views.WorkshopSpecialtyListView.as_view(), name='workshops-specialty-list'),
    path('workshops/maintenance/', views.LoginWorkshopListView.as_view(), name='workshops-maintenance-list'),
    path('workshops/maintenance/professional/<int:pk>/', views.LoginWorkshopProfessionalListView.as_view(), name='workshops-professional-maintenance-list'),
    path('workshops/create/', views.WorkshopCreateView.as_view(), name='workshops-create'),
    path('workshops/update/<int:pk>/', views.WorkshopUpdateView.as_view(), name='workshops-update'),
    path('workshops/delete/<int:pk>/', views.WorkshopDeleteView.as_view(), name='workshops-delete'),
]
