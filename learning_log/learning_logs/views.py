from django.shortcuts import render

from .models import Topic

def index(request):
     """The home page for Learning Log."""
     
     return render(request, 'learning_logs/index.xhtml')

def topics(request):
     """Show all topics"""
     
     # We query the database by asking for the Topic objects, sorted by the 
     # created_at attribute
     topics = Topic.objects.order_by('created_at')

     # A context is a dictionary in which the keys are names we’ll use in the 
     # template to access the data we want, and the values are the data we need 
     # to send to the template
     context = {'topics': topics}
     return render(request, 'learning_logs/topics.xhtml', context)
