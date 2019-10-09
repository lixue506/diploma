from .views import home,admin
from django.urls import path

app_name = 'acmxs'
urlpatterns = [
    path('/', home.welcome, name='index')
]