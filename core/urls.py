from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientes.views import ClienteViewSet
from produtos.views import ProdutoViewSet
from vendas.views import VendaViewSet
from relatorios.views import DashboardRelatorioView, DashboardTemplateView
from clientes.views import ClienteViewSet, ClientesTemplateView
from produtos.views import ProdutoViewSet, ProdutosTemplateView # <-- Atualize a importação
from vendas.views import VendaViewSet, VendasTemplateView #

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # Rota da API que calcula e devolve os dados em JSON
    path('api/relatorios/dashboard/', DashboardRelatorioView.as_view(), name='dashboard_relatorio'),
    
    # ROTA VISUAL: Endereço para abrir a tela bonita no seu navegador!
    path('dashboard/', DashboardTemplateView.as_view(), name='visual_dashboard'),
    path('clientes/', ClientesTemplateView.as_view(), name='visual_clientes'),
    path('produtos/', ProdutosTemplateView.as_view(), name='visual_produtos'),
    path('vendas/', VendasTemplateView.as_view(), name='visual_vendas'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]