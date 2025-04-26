from django.db import models

class Usuario(models.Model):
    
    id_usuario=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=30)
    idade=models.IntegerField()
    voto = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.idade}) - {self.voto or 'Sem voto'}"


