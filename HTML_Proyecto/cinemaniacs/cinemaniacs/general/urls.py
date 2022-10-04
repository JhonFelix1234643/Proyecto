from django.urls import path
from index import views

urlpatterns = [
    path('',views.VistaInicio.as_view(),name="index"),
]