from django.db import models

class Project(models.Model): # Clase que hereda los modelos de Django
    # Atributos que se guardan en la tabla
    name = models.CharField(max_length=200) # Campo de nombre tipo texto de máximo 200 caracteres.

    def __str__(self): # Método que retorna el nombre del proyecto como String
        return self.name

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} - Proyecto: {self.project.name}'