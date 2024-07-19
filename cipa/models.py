from django.db import models

class Membro(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Reuniao(models.Model):
    data = models.DateTimeField()
    pauta = models.TextField()
    membros_presentes = models.ManyToManyField(Membro)

    def __str__(self):
        return f"Reunião em {self.data.strftime('%d/%m/%Y %H:%M')}"
