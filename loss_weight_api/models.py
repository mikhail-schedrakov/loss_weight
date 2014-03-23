from django.db import models

# Anthropometry data of user
class anth(models.Model):
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    current_waight = models.DecimalField(max_digits=3, decimal_places=2)
    initial_waight = models.DecimalField(max_digits=3, decimal_places=2)
    email = models.CharField(max_length=200)
    height = models.IntegerField()
    password = models.CharField(max_length=200)
    registration_date = models.DateField(auto_now_add=True)



class CheckPoint(models.Model):
    date = models.DateField()
    isPlanned = models.BooleanField()
    weight = models.DecimalField(max_digits=3, decimal_places=2)
    # Relations
    user = models.ForeignKey(User)