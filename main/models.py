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




