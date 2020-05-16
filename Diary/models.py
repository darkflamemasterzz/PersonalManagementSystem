from django.db import models
from User.models import User, Tag

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title
