from django.urls import path
from .views.views import MovieList

app_name = 'core'

urlpatterns = [
    path('', MovieList.as_view(), name='MovieList'),
]
