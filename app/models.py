from django.db import models

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
