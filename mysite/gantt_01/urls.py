from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'gantt_01'

urlpatterns = [
    path('', views.index, name='index'),
]