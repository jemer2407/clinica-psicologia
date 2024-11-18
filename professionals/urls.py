from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('professionals/', views.ProfessionalsListView.as_view(), name='professionals-list'),
    path('professionals/<int:pk>/<slug:slug>/', views.ProfessionalDetailView.as_view(), name='professionals-detail'), 
    path('professionals/specialty/<int:pk>/', views.ProfessionalBySpecialtyListView.as_view(), name='professional-specialty-list'),
    path('professionals/maintenance/', views.LoginProfessionalsListView.as_view(), name='professionals-maintenance-list'),
    path('professionals/maintenance/specialty/<int:pk>/', views.LoginProfessionalBySpecialtyListView.as_view(), name='professionals-specialty-maintenance-list'),
    path('professionals/create/', views.ProfessionalCreateView.as_view(), name='professional-create'),
    path('professionals/update/<int:pk>/', views.ProfessionalUpdateView.as_view(), name='professional-update'),
    path('professionals/delete/<int:pk>/', views.ProfessionalDeleteView.as_view(), name='professional-delete'),
]



# Ruta imagenes para que se muestren en el panel de administrador cuando estemos en desarrollo (settings.DEBUG == True)

if settings.DEBUG:
    from django.conf.urls.static import static
    # variables MEDIA_URL Y MEDIA_ROOT las tenemos que declarar en el settings del proyecto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)