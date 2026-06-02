from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from produtos.models import Produto

class Venda(models.Model):
    # ALTERADO: on_delete alterado para SET_NULL para permitir excluir o cliente sem quebrar o histórico de faturamento
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='vendas'
    )
    
    # MANTIDO: Vincula ao admin/funcionário logado
    usuario = models.ForeignKey(
        User, 
        on_delete=models.PROTECT,
        related_name='vendas_realizadas'
    )
    
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Tratamento caso o cliente tenha sido deletado do sistema
        cliente_nome = self.cliente.nome if self.cliente else "Cliente Removido"
        return f"Venda {self.id} - {cliente_nome}"

    def atualizar_total(self):
        """
        Método auxiliar: Se você começar a usar a tabela ItemVenda,
        este método soma os subtotais dos itens e atualiza o total da venda.
        """
        total_itens = self.itens.aggregate(total_somado=models.Sum('subtotal'))['total_somado'] or 0.00
        self.total = total_itens
        self.save()


class ItemVenda(models.Model):
    # MANTIDO: Se a venda master for deletada, os itens dela somem em cascata
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    
    # MANTIDO: Bloqueia a exclusão do produto se ele já estiver em alguma venda
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='itens_venda')
    
    quantidade = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
        
    def save(self, *args, **kwargs):
        """
        Garante que o subtotal seja calculado automaticamente antes de salvar,
        multiplicando o preço do produto pela quantidade.
        """
        if self.produto and self.quantidade:
            self.subtotal = self.produto.preco * self.quantidade
        super().save(*args, **kwargs)
        # Atualiza o valor total da venda mãe
        self.venda.atualizar_total()