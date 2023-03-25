from django.db import models
# criar os modelos de dados ou seja nossas classes, persistir dentro do banco de dados

class Produto1(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits = 9)
    estoque = models.IntegerField('Quantidade em Estoque')
    marca = models.CharField('Marca', max_length=100)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'
