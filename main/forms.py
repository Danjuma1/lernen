from django import forms
from .models import Topic, Entry

# Topic form
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        label = {'test': ''}

# Entry form
class EntryForm(forms.ModelForm):
    model = Entry
    fields = ["text"]
    label = {'text': ''}
    widget = {'text': forms.Textarea(attrs={'cols': 80})}
    