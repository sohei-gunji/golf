from django.db import models

# Create your models here.
class HDCPGroups(models.Model):
    group = models.CharField(max_length=1, null=False, blank=False)
    lower = models.SmallIntegerField(default=0)
    upper = models.SmallIntegerField(default=0)
