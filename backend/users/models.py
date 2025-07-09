from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.BigAutoField(primary_key=True, null = False)
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False, unique= True)
    password = models.CharField(max_length=255, null=False)

    class Meta:
        db_table= "users"
        managed= True