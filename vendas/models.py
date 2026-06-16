from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from produtos.models import Produto

class Venda(models.Model):
    # ALTERADO: on_delete alterado para SET_NULL para permitir excluir o cliente sem quebrar o histórico
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
    
    # Campo para armazenar o valor total acumulado da venda
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Tratamento caso o cliente tenha sido deletado do sistema
        cliente_nome = self.cliente.nome if self.cliente else "Cliente Removido"
        return f"Venda ({self.id}) - {cliente_nome}"

    def atualizar_total(self):
        """
        Método auxiliar: Soma os subtotais dos itens vinculados 
        e atualiza o total da venda automaticamente.
        """
        # Busca a soma de todos os subtotais dos itens desta venda
        resultado = self.itens.aggregate(total_somado=models.Sum('subtotal'))
        total_itens = resultado.get('total_somado') or 0.00
        
        # Atualiza o campo total da venda
        self.total = total_itens
        # Salva usando update_fields para evitar loops de save() com o ItemVenda
        Venda.objects.filter(pk=self.pk).update(total=total_itens)

    @property
    def quantidade_itens(self):
        """
        Retorna a quantidade total de produtos dentro desta venda.
        Soma as quantidades de cada ItemVenda.
        """
        resultado = self.itens.aggregate(total_qtd=models.Sum('quantidade'))
        return resultado.get('total_qtd') or 0


class ItemVenda(models.Model):
    # MANTIDO: Se a venda master for deletada, os itens dela somem em cascata
    venda = models.ForeignKey(
        Venda, 
        on_delete=models.CASCADE, 
        related_name='itens'
    )
    
    # MANTIDO: Bloqueia a exclusão do produto se ele já estiver em alguma venda
    produto = models.ForeignKey(
        Produto, 
        on_delete=models.PROTECT, 
        related_name='itens_venda'
    )
    
    quantidade = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"

    def save(self, *args, **kwargs):
        """
        Garante que o subtotal seja calculado automaticamente antes de salvar,
        multiplicando o preço do produto pela quantidade.
        """
        if self.produto and self.quantidade:
            # CORRIGIDO: Cálculo correto do subtotal multiplicando preço por quantidade
            self.subtotal = self.produto.preco * self.quantidade
            
        super().save(*args, **kwargs)
        
        # Atualiza o valor total da venda mãe após salvar o item
        self.venda.atualizar_total()

    def delete(self, *args, **kwargs):
        """
        Garante que se um item for removido da sacola, o total da venda 
        seja recalculado.
        """
        venda_mae = self.venda
        super().delete(*args, **kwargs)
        venda_mae.atualizar_total()