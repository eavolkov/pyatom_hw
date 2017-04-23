from django.shortcuts import render
from .forms import CreateForm, EditForm

def initial_view(request=None, info=''):
    create_form = CreateForm(initial={'title_create': '', 'estimate_create': None})
    edit_form = EditForm(initial={'title_edit': '', 'state_edit': '', 'estimate_edit': None})
    return render(request, 'django_project.html', {'create_form': create_form, 'edit_form': edit_form, 'info': info})