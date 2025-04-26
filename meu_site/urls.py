from django.contrib import admin
from django.urls import path
from vota_time import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.cad_vota,name="votar"),
    path('votacao/<int:id_usuario>/', views.votacao, name='votacao')
]
