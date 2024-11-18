from django.urls import path
from .views import SpecialtyListView, SpecialtyDetailView, SpecialtyCreateView, LoginSpecialtyListView, SpecialtyUpdateView, SpecialtyDeleteView
from django.conf import settings

urlpatterns = [
    path('specialty/', SpecialtyListView.as_view(), name='specialtys-list'),
    path('specialty/<int:pk>/<slug:slug>/', SpecialtyDetailView.as_view(), name='specialtys-detail'),
    path('specialty/maintenance/', LoginSpecialtyListView.as_view(), name='specialtys-maintenance-list'),
    path('specialty/create/', SpecialtyCreateView.as_view(), name='specialty-create'),
    path('specialty/update/<int:pk>/', SpecialtyUpdateView.as_view(), name='specialty-update'),
    path('specialty/delete/<int:pk>/', SpecialtyDeleteView.as_view(), name='specialty-delete'),

]



# Ruta imagenes para que se muestren en el panel de administrador cuando estemos en desarrollo (settings.DEBUG == True)

if settings.DEBUG:
    from django.conf.urls.static import static
    # variables MEDIA_URL Y MEDIA_ROOT las tenemos que declarar en el settings del proyecto
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)