from django.db import models
from django.contrib.auth.models import User
from word.models import Word
# Create your models here.


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    phone = models.CharField(max_length=100, verbose_name='Telefono',blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
    is_admin = models.BooleanField(default=False, verbose_name='Admin') 

    def __str__(self):
        return self.user.username
    


# class UserScore(models.Model):
#     profile=models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class UserScore(models.Model):
    profile=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    word=models.ForeignKey(Word, on_delete=models.CASCADE)
    time=models.IntegerField() # en segundos
    score=models.IntegerField()
    is_resolved=models.BooleanField(default=False)

    def __str__(self):
        return self.profile.user.username