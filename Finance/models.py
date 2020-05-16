from django.db import models
from User.models import User, Tag

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    origin = models.CharField( max_length=50)
    count = models.IntegerField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.origin

class Outcome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    destination = models.CharField( max_length=50)
    outcome_type = models.BooleanField(default=True) #True(product) false(consum)
    count = models.IntegerField(default=0)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.destination
