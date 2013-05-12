from django.db import models

class Songs(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    url = models.CharField()
    phone_number = models.CharField()
    length = models.IntegerField()
    score = models.IntegerField(default=0)
