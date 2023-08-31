
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listar_aprendices, name='listar_aprendices'),
    path('crear/', views.crear_aprendiz, name='crear_aprendiz'),
    path('<int:aprendiz_id>/', views.ver_aprendiz, name='ver_aprendiz'),
    path('<int:aprendiz_id>/editar/', views.editar_aprendiz, name='editar_aprendiz'),
    path('<int:aprendiz_id>/eliminar/', views.eliminar_aprendiz, name='eliminar_aprendiz'),
]
