from django.db import models

class Songs(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    url = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=50)
    length = models.IntegerField()
    score = models.IntegerField(default=0)
