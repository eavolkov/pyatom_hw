from django.shortcuts import render
from .forms import CreateForm, EditForm, DeleteForm

def initial_view(request=None, info=''):
    create_form = CreateForm(initial={'title_create': '', 'estimate_create': None})
    edit_form = EditForm(initial={'title_edit': '', 'state_edit': '', 'estimate_edit': None})
    delete_form = DeleteForm(initial={'title_delete': ''})
    return render(request, 'django_project.html', {'create_form': create_form, 'edit_form': edit_form, 'delete_form': delete_form, 'info': info})
