from rest_framework import serializers
from .models import Venda, ItemVenda

class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    itens = ItemVendaSerializer(many=True, read_only=True)  # Mostra os itens inclusos na venda

    class Meta:
        model = Venda
        fields = '__all__'