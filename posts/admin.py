from django.contrib import admin
from marketing.models import Signup

from .models import Author, Category, Post, Comment, PostView, Galery, FotolarGornusler, Fotolar, Audio_kid, Audio, Video_kid, Video, Paper_kid, Paper, Magazine_kid, Magazine, Hobby_kid, Hobby

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Signup)
admin.site.register(Galery)
admin.site.register(FotolarGornusler)
admin.site.register(Fotolar)
admin.site.register(Audio_kid)
admin.site.register(Audio)
admin.site.register(Video_kid)
admin.site.register(Video)
admin.site.register(Paper_kid)
admin.site.register(Paper)
admin.site.register(Magazine_kid)
admin.site.register(Magazine)
admin.site.register(Hobby_kid)
admin.site.register(Hobby)