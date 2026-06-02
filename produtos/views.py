from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

from django.views.generic import TemplateView

class ProdutosTemplateView(TemplateView):
    template_name = 'produtos.html'