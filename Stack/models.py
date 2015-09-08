from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SHORT_NAME_MAX_LENGTH = 18

def Concatenate(str_value, max_length=SHORT_NAME_MAX_LENGTH):
    return str_value[:max_length-3].strip() + '...'

class Stack(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'name')

    def concatenated_name(self):
        return Concatenate(self.name)

    def get_contents(self):
        return Note.objects.filter(stack=self, popped=False).order_by('-time_created')
        # Maybe list(Note.objects.filter(stack=self, popped=False).order_by('time_created'))

    def latest(self):
        return Note.objects.filter(stack=self, popped=False).latest()

    def pop(self):
        top = self.peek()
        top.popped = True
        top.save()

    def peek(self):
        return self.latest()

    def pop_and_peek_next(self):
        self.pop()
        return self.peek()

class Note(models.Model):
    stack = models.ForeignKey(Stack)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    popped = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('stack', 'time_created')
        get_latest_by = 'time_created'

    def concatenated_title(self):
        return Concatentate(self.title)
