from django.contrib import admin

# Register your models here.

from clapp.models import Post,Image,Tag

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Tag)
