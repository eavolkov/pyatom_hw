from django.shortcuts import render

from .forms import CreateForm


def view_create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        info = 'Форма заполнена, но некорректна'
        if form.is_valid():
            info = 'Форма заполнена и корректна'
    else:
        info = 'Форма не заполнена'
        form = CreateForm(initial={'title': '', 'estimate': None})

    return render(
        request, 'example.html',
        {'form': form, 'info': info}
    )
