from django.urls import path
from . import views 

urlpatterns = [
    path('api/timbrar_impap', views.timbrar_impap, name = 'timbrar_impap' ),
    path('api/timbrar_rh', views.timbrar_rh, name = 'timbrar_rh' ),
    path('api/timbrar_paper', views.timbrar_paper, name = 'timbrar_paper' ),
    path('api/timbrar_mobix', views.timbrar_mobix, name = 'timbrar_mobix' ),
    #Test Urls
    path('api/timbrar_impap_test', views.timbrar_impap_test, name = 'timbrar_impap_test' ),
    path('api/timbrar_rh_test', views.timbrar_rh_test, name = 'timbrar_rh_test' ),
    path('api/timbrar_paper_test', views.timbrar_paper_test, name = 'timbrar_paper_test' ),
    path('api/timbrar_mobix_test', views.timbrar_mobix_test, name = 'timbrar_mobix_test' ),
]