from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome
