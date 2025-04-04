from django.db import models


# Create your models here.

class Folder(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    content = models.TextField()
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='documents')

    def __str__(self):
        return self.name
