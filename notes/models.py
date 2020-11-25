from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=264)
    #email = models.EmailField()
    #text= models.CharField(max_length=264)
    contact = models.TextField()

    class Meta:
        db_table = "employee"
