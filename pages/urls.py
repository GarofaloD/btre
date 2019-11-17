from django.urls import path
from . import views

urlpatterns = [ #Pattern for the url itself. This is not the content
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]