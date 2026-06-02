from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count
from vendas.models import Venda, ItemVenda

# Importação necessária para renderizar páginas HTML tradicionais
from django.views.generic import TemplateView

class DashboardRelatorioView(APIView):
    permission_classes = [IsAuthenticated] # Mantém a segurança JWT ativa

    def get(self, request):
        # 1. Faturamento Total do sistema
        faturamento_total = Venda.objects.aggregate(total=Sum('total'))['total'] or 0.00
        
        # 2. Total de vendas realizadas
        total_vendas = Venda.objects.count()
        
        # 3. Total de itens de produtos comercializados
        total_itens_vendidos = ItemVenda.objects.aggregate(total_qtd=Sum('quantidade'))['total_qtd'] or 0
        
        # Monta o JSON de resposta
        dados_dashboard = {
            "faturamento_total": float(faturamento_total),
            "total_vendas_realizadas": total_vendas,
            "total_itens_comercializados": total_itens_vendidos,
        }
        
        return Response(dados_dashboard)


# --- NOVA VIEW NO FINAL DO ARQUIVO PARA CARREGAR O HTML ---
class DashboardTemplateView(TemplateView):
    template_name = 'dashboard.html'