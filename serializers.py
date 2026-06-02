from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  # Isso diz para a API trazer todos os campos (id, nome, cpf, email, telefone)