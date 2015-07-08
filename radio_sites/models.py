from django.db import models

class RadioSite(models.Model):
    name=models.CharField(max_length=200,verbose_name="电台名称")

# Create your models here.
