from django.urls import path
from . import views

app_name = 'bill'
urlpatterns = [ 
    path('', views.index, name='index'),
]