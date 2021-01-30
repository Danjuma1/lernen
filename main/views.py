from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# view for index page 
def index(request):
    return render(request, '')

# topics view (all topics)
def topics(request):
    # show all topics arraged by date added
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, '', context)

# topic view (individual topic)
def topic(request, topic_id):
    # show a single topic and all its entries
    topic = Topic.objects.get(id=topic_id)
    # make sure the topic belongs to d current user
    if topic.owner != request.user:
        raise Http404
    
    # entries for the topic (arranged by date added)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, '', context)

# view for creating new topic
def new_topic(request):
    # Adding a new topic
    if request.method != 'POST':
        # If form method isn't POST, no data submitted, it'll create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse(''))

    context = {'form': form}
    return render(request, '', context)