from django.urls import path
from .views import *
from rest_framework import routers


# router= routers.DefaultRouter()
# router.register(r'users', RegisterUserView, 'users')

urlpatterns = [ 
    path('api/register/', RegisterUserView.as_view(), name='register_user'),

    # path('listado', RegisterUserView.as_view(), name='list_word'),
    # path('agregar_palabra', WordFormView.as_view(), name='add_word'),
    # path('delete_word/<int:pk>/', WordDeleteView.as_view(), name='delete_word'),

    # path('api/words', WordListAPI.as_view(), name='list_word_api'),
]