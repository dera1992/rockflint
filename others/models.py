from django.db import models
from account.models import Profile

# Create your models here.

class Information (models.Model):
    name = models.CharField(max_length=300,blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.subject

class Testimony (models.Model):
    comment = models.TextField()
    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE)
    position = models.CharField(max_length=300, blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.position