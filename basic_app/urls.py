from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('questions/', Question.as_view(), name='questionHub')
]
