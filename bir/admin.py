from django.contrib import admin

from .models import Users, Singer, Section, Music

admin.site.register(Users)
admin.site.register(Singer)
admin.site.register(Section)
admin.site.register(Music)