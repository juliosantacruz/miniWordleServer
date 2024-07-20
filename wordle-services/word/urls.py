from django.urls import path
from .views import *




urlpatterns = [ 
    path('listado', WordListView.as_view(), name='list_word'),
    path('agregar_palabra', WordFormView.as_view(), name='add_word'),
    path('delete_word/<int:pk>/', WordDeleteView.as_view(), name='delete_word'),
]