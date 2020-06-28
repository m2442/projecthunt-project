from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    pub_date = models.DateTimeField()
    body = models.TextField()

    icon = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)


    def __str__(self):
        return self.title
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    def top_para(self):
        return self.body.split("<changemypara>")[0]
    def mid_para(self):
        return self.body.split("<changemypara>")[1]
    def bottom_para(self):
        return self.body.split("<changemypara>")[2]
