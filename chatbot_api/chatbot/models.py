from django.db import models

# Create your models here.

class Chatbot(models.Model):
    numero_opcion = models.CharField(max_length=30)
    pregunta = models.CharField(max_length=100)
    respuesta = models.CharField(max_length=200)
    categorias = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pregunta
