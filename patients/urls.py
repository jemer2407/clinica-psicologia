from django.urls import path
from . import views

from django.conf import settings

urlpatterns = [
    #urls de pacientes
    path('patients/', views.PatientListView.as_view(), name='patients-list'),
    path('patients/create/', views.PatientCreateView.as_view(), name='patient-create'),
    path('patients/update/<int:pk>/', views.PatientUpdateView.as_view(), name='patient-update'),
    path('patients/delete/<int:pk>/', views.PatientDeleteView.as_view(), name='patient-delete'),
    path('patients/professional/<int:pk>/', views.PatientsOfProfessionalListView.as_view(), name='patients-professional-list'),

    #urls de compañia medica
    path('companies/', views.CompanyListView.as_view(), name='companies-list'),
    path('companies/create/', views.CompanyCreateView.as_view(), name='companies-create'),
    path('companies/update/<int:pk>/', views.CompanyUpdateView.as_view(), name='companies-update'),
    path('companies/delete/<int:pk>/', views.CompanyDeleteView.as_view(), name='companies-delete'),
]



# Ruta imagenes para que se muestren en el panel de administrador cuando estemos en desarrollo (settings.DEBUG == True)

if settings.DEBUG:
    from django.conf.urls.static import static
    # variables MEDIA_URL Y MEDIA_ROOT las tenemos que declarar en el settings del proyecto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)