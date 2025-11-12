from django.db import models

# Create your models here.

class BookModel(models.Model):
    title = models.CharField(max_length=30)
    author = models. CharField(max_length=30)
    description = models. TextField()
    pages = models. IntegerField()
    is_new = models.BooleanField()
    price = models. IntegerField()
    def __str__(self):
        return str(self.price)
