from django.urls import path
from . import views 

urlpatterns = [
    path('get_cuentas_por_pagar', views.get_cuentas_por_pagar, name='get_cuentas_por_pagar'),
    path('get_cuentas_por_cobrar', views.get_cuentas_por_cobrar, name='get_cuentas_por_cobrar'),
]