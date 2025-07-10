from django.urls import path
from . import views

urlpatterns = [
   path('probar/', views.incio,),
   path('', views.pagina_cafe,),


]