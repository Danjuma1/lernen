from django.db import models
from django.contrib.auth.models import User

# Topic Model
class Topic(models.Model):
    # A topic the user is learning about
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Returns the topic text
        return self.text

# Entry Model
class Entry(models.Model):
    # Something user have learnt
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # Returns first 50 letters of the entry
        return self.text[:50] + "..."




