from django.contrib import admin
from User.models import User, UserBook, UserMovie, Tag

admin.site.register(User)
admin.site.register(UserBook)
admin.site.register(UserMovie)
admin.site.register(Tag)
