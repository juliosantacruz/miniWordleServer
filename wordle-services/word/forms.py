from django import forms
from .models import *


class WordForm(forms.Form):
    word=forms.CharField(max_length=8, label='Palabra')
    description=forms.CharField(max_length=360, label='Descripcion')
    url=forms.URLField(label='Link',required=False)
    image=forms.ImageField( label='Imagen',required=False)
    category=forms.ModelChoiceField(queryset=Category.objects.all(), label='Categoria')
    # created_at=forms.DateTimeField(label='Fecha de creacion',)
    # word_size = forms.IntegerField(label='tamanio',blank=True, null=True)
        
    # Crear un producto desde el mismo formulario
    def save(self):
        Word.objects.create(
            word = self.cleaned_data['word'],
            description = self.cleaned_data['description'],
            url= self.cleaned_data['url'],
            image=self.cleaned_data['image'],
            category=self.cleaned_data['category']
        )