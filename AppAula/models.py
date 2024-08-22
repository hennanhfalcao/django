from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length = 100)
    sobrenome = models.CharField(max_length = 100)

    def _str_(self):
        return f"{self.nome} {self.sobrenome}"
    
    #MAKEMIGRATIONS E MIGRATE SÓ SÃO UTILIZADOS PARA ATUALIZAR O ESCOPO DA CLASSE PRINCIPAL