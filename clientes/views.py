from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

from django.views.generic import TemplateView

class ClientesTemplateView(TemplateView):
    template_name = 'clientes.html'