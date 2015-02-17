from django.db import models

# Create your models here.
class Users_git_data(models.Model):
    name = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100)
    payload = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name