from django.db import models
class ChannelItem(models.Model):
    name=models.CharField(max_length=200)
    audio_file_path=models.CharField(max_length=200)
    time_begin=models.DateTimeField()
    time_end=models.DateTimeField()
    times_played=models.IntegerField(verbose_name="被推送(播放)的次数")
    is_expired=models.BooleanField(verbose_name="是否已经过期")

# Create your models here.
