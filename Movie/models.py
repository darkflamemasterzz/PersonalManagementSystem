from django.db import models
from django.utils.translation import gettext_lazy as _

class Movie(models.Model):
    class Type(models.TextChoices):
        realism = 'r', _('realism') 
        love = 'l', _('love')
        science = 's', _('science')
    name = models.CharField(max_length=50)
    director = models.CharField( max_length=10)
    description = models.TextField()
    type = models.CharField(choices=Type.choices, 
                            max_length=20,
                            default=Type.realism,)
    publish_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
