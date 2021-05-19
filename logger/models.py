from django.db import models

# Create your models here.
class FileUploadModel(models.Model):
    name        = models.CharField(max_length=100)
    file_upload = models.FileField()

    def __str__(self):
        return self.name
