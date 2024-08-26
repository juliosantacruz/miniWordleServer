from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .forms import *
from .serializer import WordSerializer
import random
# Create your views here.

class WordFormView(generic.FormView):
    template_name='add_word.html'
    form_class=WordForm
    success_url=reverse_lazy('add_word')

    def get_context_data(self, **kwargs):
        context = super(WordFormView, self).get_context_data(**kwargs)
        context['word_list'] = Word.objects.all()  
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class WordListView(generic.ListView):
    model= Word
    template_name='list_word.html'
    context_object_name='words'


class WordDeleteView(View):
    def post(self, request, *args, **kwargs):
        word_id = self.kwargs.get('pk')
        word = Word.objects.get(id=word_id)
        word.delete()
        return HttpResponseRedirect(reverse('add_word'))
    

class WordListAPI(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, resquest):
        words = Word.objects.all()
        serializer= WordSerializer(words, many=True)

        return Response(serializer.data)
    
class WordDayAPI(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, resquest):
        words = Word.objects.all()
        word = random.choice(words)
        print(word)
        serializer= WordSerializer(word )

        return Response(serializer.data)