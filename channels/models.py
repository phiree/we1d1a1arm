from django.db import models
from radio_sites import models as radio_sites_models
class Channel(models.Model):
    name=models.CharField(max_length=200,verbose_name="分类名称")
    description=models.CharField(max_length=2000,verbose_name="分类介绍")
    create_date=models.DateTimeField(verbose_name="创建时间")
    channel_belong_to=models.ForeignKey(radio_sites_models.RadioSite,verbose_name="所属电台")
    podcastor=models.CharField(max_length=20,verbose_name="播音人")
    ads_image=models.CharField(max_length=200,verbose_name="频道广告图片地址")

