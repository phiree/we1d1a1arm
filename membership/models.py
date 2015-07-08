from django.db import models
from radio_sites import  models as radio_sites_models
class MembershipUser(models.Model):
    loginname=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    ownerof=models.ForeignKey( radio_sites_models.RadioSite,verbose_name="频道拥有者",help_text="该用户登录时会自动跳转到该频道")
# Create your models here.
