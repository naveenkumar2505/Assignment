from django.db import models

# Create your models here.

class Users(models.Model):
    id=models.CharField(primary_key=True,max_length=20)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    company_name=models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField()
    email=models.EmailField(max_length=255)
    web=models.URLField()
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
