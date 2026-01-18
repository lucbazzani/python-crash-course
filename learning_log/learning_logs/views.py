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

def topic(request, topic_id): 
    """Show a single topic and all its entries."""

    topic = Topic.objects.get(id=topic_id)
    # The minus sign in front of created_at sorts the results in reverse order
    entries = topic.entry_set.order_by('-created_at')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.xhtml', context)