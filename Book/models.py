from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    class Type(models.TextChoices):
        philosophy = 'P', _('philosophy') #??
        computer_science = 'CS', _('computer_science')
        novel = 'N', _('novel')
        economic = 'E', _('economic')
        other = 'O', _('other')
    class progress(models.IntegerChoices):
        zero = 0, _('0%')
        one = 1, _('20%')
        two = 2, _('40%')
        three = 3, _('60%')
        four = 4, _('80%')
        five = 5, _('100%')

    # user = models.ManyToManyField(User)
    book_name = models.CharField(max_length=50)
    author = models.CharField( max_length=10)
    description = models.TextField()
    book_type = models.CharField(choices=Type.choices, 
                                max_length=20,
                                default=Type.other,)
    publish_date = models.DateField(auto_now=False, auto_now_add=False)
    progress = models.IntegerField(choices=progress.choices,
                                   default=progress.zero)

    def __str__(self):
        return self.book_name
