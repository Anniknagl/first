from django.db import models
# Create your models here.


class Profile(models.Model):
    vk_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100)

    def _str__(self):
        return self.vk_id
