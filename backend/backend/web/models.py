from django.db import models


class Data(models.Model):
    coordinate_x = models.CharField(max_length=4)
    coordinate_y = models.CharField(max_length=4)
    image = models.ImageField(upload_to='media/')
