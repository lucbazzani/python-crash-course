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

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry
    # the value of id is assigned to the parameter entry_id. Django sends 
    # requests that match this format to the view function edit_entry()
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),    
]