"""Defines URL patterns for learning_logs.""" 
 
from django.urls import path 

from . import views 

app_name = 'learning_logs' 
urlpatterns = [ 
    # Home page
    path('', views.index, name='index'),

    # Page that shows all topics
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    # When Django finds a URL that matches this pattern, it calls the view 
    # function topic() with the value assigned to topic_id as an argument
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]