from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # The 'Meta' class holds extra information for managing a model; here, 
    # it lets us set a special attribute telling Django to use 'Entries' when it 
    # needs to refer to more than one entry. 
    # Without this, Django would refer to multiple entries as 'Entrys'.
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry.""" 
        
        return f"{self.text[:50]}[...]"