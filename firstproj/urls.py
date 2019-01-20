
from django.urls import path
from .views import *
from .view2 import get_credential, get_token
from rest_framework .urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', page),
    path('get_credential/', get_credential),
    path('token/', get_token),
    path('api/profiles', ProfileList.as_view()),
    path('api/profiles/<int:idP>', ProfileDetail.as_view()),
]

# не ебу за что именно это отвечает
# urlpatterns = format_suffix_patterns(urlpatterns)
