from django.db import models

class Microoganism(models.Model):
    name = models.CharField(max_length=250)
    habitat = models.CharField(max_length=250)
    morphology = models.TextField()
    biochemicals = models.TextField()
    metabolism = models.CharField(max_length=250)
    diseases = models.TextField()
    antibiotics = models.TextField()
    
    def __str__(self):
        return self.name