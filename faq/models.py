
from django.db import models

# Create your models here.



class Faq(models.Model):
    title = models.CharField(max_length=30, db_column='title')
    content = models.TextField(db_column='content')

    class Meta:
        db_table = 'faq'
        verbose_name_plural = 'Faq'