from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=100)
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)      
    def __str__(self):
        return f'{self.nome} - {self.telefone} - {self.email}'


class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING) 
    #ForeignKey lista todas as marcas para voce incluir o modelo do carro
    nome = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nome} - {self.marca.nome}'


#====================================================================================
#VEICULO
class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.DO_NOTHING)
    ano_modelo = models.IntegerField(max_length=4)
    ano_fabricacao = models.IntegerField(max_length=4)
    preco = models.DecimalField(max_digits=18, decimal_places=2)
    observacao = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.modelo} - {self.ano_modelo} - {self.ano_fabricacao} - {self.preco} - {self.observacao}'



   
        

