from rest_framework import serializers
from .models import Venda, ItemVenda


class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade', 'subtotal']
        read_only_fields = ['subtotal']


class VendaSerializer(serializers.ModelSerializer):
    itens = ItemVendaSerializer(many=True)
    quantidade_itens = serializers.ReadOnlyField()

    class Meta:
        model = Venda
        fields = '__all__'

    def create(self, validated_data):
        # 1. Remove a lista de itens para não quebrar a criação da Venda
        itens_data = validated_data.pop('itens', [])
        
        # 2. DEFESA: Se por acaso houver um campo 'quantidade' perdido no JSON principal,
        # nós removemos ele aqui para não bugar o banco de dados
        validated_data.pop('quantidade', None)

        # 3. Cria a venda master apenas com os dados limpos (cliente, usuario, total)
        venda = Venda.objects.create(**validated_data)

        # 4. Cria cada item da venda calculando o subtotal
        for item_data in itens_data:
            produto = item_data['produto']
            quantidade = item_data['quantidade']
            subtotal = produto.preco * quantidade

            ItemVenda.objects.create(
                venda=venda,
                subtotal=subtotal,
                **item_data
            )

        # 5. Atualiza o total acumulado da venda
        venda.atualizar_total()

        return venda