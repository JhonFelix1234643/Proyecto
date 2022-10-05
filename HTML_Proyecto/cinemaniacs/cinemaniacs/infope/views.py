from django.views.generic import TemplateView
from infope.models import *


#-----------------------Clase vista Bienvenida-------------------------
class VistaInicio(TemplateView):
    template_name='info/ifo_peliculas.html'
#----------------------------------------------------------------------