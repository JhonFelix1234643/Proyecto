from django.urls import path
from infope import views

urlpatterns = [
    path('',views.VistaInicio.as_view(),name="infope"),
]