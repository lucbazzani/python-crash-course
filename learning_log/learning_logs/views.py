from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

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

def new_topic(request):
     """Add a new topic"""

     if request.method != 'POST':
          # No data submitted. Create a blank form
          form = TopicForm()
     else:
          # POST data submitted. Proccess data
          form = TopicForm(data=request.POST)
          if form.is_valid():
               form.save()
               return redirect('learning_logs:topics')
          
     # Display a blank or a invalid form
     context = {'form': form}
     return render(request, 'learning_logs/new_topic.xhtml', context)

def new_entry(request, topic_id):
     """Add a new entry for a particular topic."""

     topic = Topic.objects.get(id=topic_id)

     if request.method != 'POST':
          # No data submitted. Create a blank form
          form = EntryForm()
     else:
          # POST data submitted. Proccess data
          form = EntryForm(data=request.POST)
          if form.is_valid():
               # create a new entry object and assign it to new_entry, without 
               # saving it to the database yet
               new_entry = form.save(commit=False)
               new_entry.topic = topic
               new_entry.save()
               return redirect('learning_logs:topic', topic_id=topic_id)
          
     # Display a blank or a invalid form
     context = {'topic': topic, 'form': form}
     return render(request, 'learning_logs/new_entry.xhtml', context)