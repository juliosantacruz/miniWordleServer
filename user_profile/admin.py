from django.contrib import admin
from .models import *

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    model=UserProfile
    

class UserScoreAdmin(admin.ModelAdmin):
    model=UserScore


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserScore, UserScoreAdmin)