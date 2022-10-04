
from django.views.generic import TemplateView
from index.models import *


#-----------------------Clase vista Bienvenida-------------------------
class VistaInicio(TemplateView):
    template_name='index/index.html'