from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=12, verbose_name='categoria')
    image= models.ImageField(upload_to='category', verbose_name='imagen', blank=True, null=True)
    
    def __str__(self):
        return self.name


class Word(models.Model):
    word=models.CharField(max_length=8, verbose_name='palabra')
    description=models.CharField(max_length=360, verbose_name='descripcion')
    url=models.URLField(verbose_name='link', blank=True, null=True)
    image=models.ImageField(upload_to='word', verbose_name='imagen', blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='categoria')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    word_size = models.IntegerField(verbose_name='tamanio',blank=True, null=True)

    def save(self, *args, **kwargs):
        self.word_size = len(self.word)
        super().save(*args, **kwargs)
        
    def __str__(self):
        wordlenght = len(self.word)
        # print(wordlenght)
        return f"{self.word} - {wordlenght}"