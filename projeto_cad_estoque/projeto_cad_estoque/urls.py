
from django.urls import path
from app_cad_estoque import views

urlpatterns = [
  # Rota, view resposável nome de referência
  # Usuarios.com
  path('',views.home,name='home'), 
  
]
