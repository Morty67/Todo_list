from django.contrib.auth.decorators import login_required
from django.views import generic

from todo.models import (
    Task,
)


class TaskListView(generic.ListView):
    model = Task
