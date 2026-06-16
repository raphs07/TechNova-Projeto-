from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth  # <-- IMPORTANTE: Para agrupar por mês
from vendas.models import Venda, ItemVenda

# Importação necessária para renderizar páginas HTML tradicionais
from django.views.generic import TemplateView

class DashboardRelatorioView(APIView):
    # 🎯 ESTAS DUAS LINHAS JUNTAS VÃO DERRUBAR O BLOQUEIO 403 DO DASHBOARD:
    authentication_classes = []  # Desativa a validação do token JWT global
    permission_classes = [AllowAny] # Permite que a tela busque os dados livremente

    def get(self, request):
        # 1. Faturamento Total do sistema
        faturamento_total = Venda.objects.aggregate(total=Sum('total'))['total'] or 0.00
        
        # 2. Total de vendas realizadas
        total_vendas = Venda.objects.count()
        
        # 3. Total de itens de produtos comercializados
        total_itens_vendidos = ItemVenda.objects.aggregate(total_qtd=Sum('quantidade'))['total_qtd'] or 0
        
        # 4. Cálculo do Lucro Total Estimado (Usando uma margem padrão de 60% sobre o faturamento)
        lucro_total = float(faturamento_total) * 0.60

        # 5. Buscar o histórico de vendas agrupado por mês para o novo gráfico
        historico_mensal = (
            Venda.objects.annotate(mes=TruncMonth('data_venda'))
            .values('mes')
            .annotate(total_mes=Sum('total'))
            .order_by('mes')
        )

        # Dicionário simples para mapear os números dos meses para nomes fáceis de ler
        meses_nomes = {
            1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr", 5: "Mai", 6: "Jun",
            7: "Jul", 8: "Ago", 9: "Set", 10: "Out", 11: "Nov", 12: "Dez"
        }

        # Listas que o Chart.js vai ler para montar a linha do gráfico
        grafico_labels = []
        grafico_lucro = []

        for registro in historico_mensal:
            if registro['mes']:
                data_mes = registro['mes']
                label = f"{meses_nomes[data_mes.month]}/{str(data_mes.year)[2:]}" # Ex: Jun/26
                lucro_do_mes = float(registro['total_mes']) * 0.60
                
                grafico_labels.append(label)
                grafico_lucro.append(round(lucro_do_mes, 2))

        # Se o seu banco estiver totalmente zerado (sem nenhuma venda ainda), criamos um padrão
        if not grafico_labels:
            grafico_labels = ["Neste Mês"]
            grafico_lucro = [round(lucro_total, 2)]

        # Monta o JSON de resposta super completo
        dados_dashboard = {
            "faturamento_total": float(faturamento_total),
            "total_vendas_realizadas": total_vendas,
            "total_itens_comercializados": total_itens_vendidos,
            "lucro_total": lucro_total,          # <-- Novo dado para o Card de Lucro
            "grafico_labels": grafico_labels,    # <-- Meses ordenados para o Gráfico
            "grafico_lucro": grafico_lucro,      # <-- Apenas valores de lucro para o Gráfico
        }
        
        return Response(dados_dashboard)


# --- NOVA VIEW NO FINAL DO ARQUIVO PARA CARREGAR O HTML ---
class DashboardTemplateView(TemplateView):
    template_name = 'dashboard.html'