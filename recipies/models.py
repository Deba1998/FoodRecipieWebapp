
from django.db import models

# Create your models here.

class Recipedetails(models.Model):
    name=models.TextField(max_length=150)
    desc=models.TextField(max_length=280)
    prikey=models.TextField(max_length=10, primary_key=True)
    ingredients=models.TextField()
    instructions=models.TextField()
    


