from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255,null=True,blank=True)
    photo = models.ImageField(upload_to='profile/%Y/%m/%d/',blank=True, default='profile/None/no-img.jpg')

    def __str__(self):
        return "confirmation for %s" % self.first_name

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)