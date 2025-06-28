from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.


class ListTasks(ListView, LoginRequiredMixin):
    model = Task
    template_name = 'task/list_task.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class DeleteTask(DeleteView, LoginRequiredMixin):
    model = Task
    success_url = '/task/list_task/'


class ToggleTaskView(View, LoginRequiredMixin, ):
    def post(self, request, id):
        task = get_object_or_404(Task, id=id, owner=self.request.user)
        task.completed = not task.completed
        task.save()
        return redirect('task_list')


class UpdateTaskView(UpdateView, LoginRequiredMixin):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = "task/edit_task.html"
    success_url = '/task/list_task/'

    def form_valid(self, form):
        form.instance.updated_at = timezone.now()
        form.instance.is_edited = True
        form.save()
        return redirect('task_list')


class AddTask(CreateView, LoginRequiredMixin):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = '/task/list_task/'
    template_name = 'task/add_task.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return redirect('task_list')
