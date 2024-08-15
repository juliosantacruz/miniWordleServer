from django.urls import path
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenRefreshView)
from rest_framework_simplejwt.views import TokenVerifyView

# router= routers.DefaultRouter()
# router.register(r'users', RegisterUserView, 'users')

urlpatterns = [ 
    path('api/register/', RegisterUserView.as_view(), name='register_user'),
    path('api/login/', MyTokenObteainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('api/user/score', UserScoreAPI, name='user_score_api'),
    path('api/user/words', UserWordsAPI, name='user_words_api'),

]