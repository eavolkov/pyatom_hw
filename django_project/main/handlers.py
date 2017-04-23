from main.roadmap import Roadmap, Task
from main.views import initial_view
from .forms import CreateForm, EditForm, DeleteForm

roadmap = Roadmap([])

def create_handler(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        info = 'Create request was done successfully'
        try:
            title, date = form.get_data_to_create()
            task = Task(title, "in_progress", date)
            roadmap.add_task(task)
        except ValueError as e:
            info = str(e)
        except AssertionError as e:
            info = str(e)
    else:
        info = 'Incorrect request'
    return initial_view(request, info)

def edit_handler(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        info = 'Edit request was done successfully'
        try:
            title, state, date = form.get_data_to_edit()
            task = Task(title, state, date)
            if not roadmap.set_task(task):
                info = "Incorrect data: Task with name %s was not found" % task.title
        except ValueError as e:
            info = str(e)
        except AssertionError as e:
            info = str(e)
    else:
        info = 'Incorrect request'
    return initial_view(request, info)

def delete_handler(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        info = 'Delete request was done successfully'
        try:
            title = form.get_data_to_delete()
            if not roadmap.delete_task(title):
                info = "Incorrect data: Task with name %s was not found" % title
        except AssertionError as e:
            info = str(e)
    else:
        info = 'Incorrect request'
    print (info)
    return initial_view(request, info)
