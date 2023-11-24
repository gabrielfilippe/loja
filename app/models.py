from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, 
                                  on_delete=models.CASCADE)
    preco = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.categoria}{self.nome}'
