from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = RichTextUploadingField()
    data_publicacao = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.titulo
