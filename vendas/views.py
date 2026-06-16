from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Venda
from .serializers import VendaSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    
    # 🎯 ESTAS DUAS LINHAS JUNTAS VÃO DERRUBAR O BLOQUEIO 403:
    authentication_classes = []  # Remove qualquer exigência de token global
    permission_classes = [AllowAny]  # Permite qualquer requisição

from django.views.generic import TemplateView

class VendasTemplateView(TemplateView):
    template_name = 'vendas.html'