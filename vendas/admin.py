from django.contrib import admin
from .models import Venda, ItemVenda

# Configuração extra para incluir os itens da venda na mesma tela da venda
class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]
    list_display = ['id', 'cliente', 'total', 'data_venda']

admin.site.register(Venda, VendaAdmin)