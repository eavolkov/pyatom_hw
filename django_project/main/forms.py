from django.forms import Form, fields, widgets
from datetime import datetime


class CreateForm(Form):

    title_create = fields.CharField(
        label='Title',
        required=True, max_length=128,
        widget=widgets.Textarea(
            attrs={'class': 'title_create'}
        )
    )

    estimate_create = fields.DateField(
        label='Estimate',
        required=True, input_formats=['%d-%m-%Y'],
        widget=widgets.DateInput(
            attrs={'class': 'estimate_create'}
        )
    )

    def get_data_to_create(self):
        title = self.data.get("title_create")
        date = self.data.get("estimate_create")
        try:
            date = datetime.strptime(date, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Incorrect data! Date should have format 'dd-mm-yyyy'")
        if date <= datetime.now().date():
            raise ValueError("Incorrect data! Date can't be less than today")
        return (title, date)


class EditForm(Form):

    title_edit = fields.CharField(
        label='Title',
        required=True, max_length=128,
        widget=widgets.Textarea(
            attrs={'class': 'title_edit'}
        )
    )

    state_edit = fields.CharField(
        label='State',
        required=True,
        widget=widgets.DateInput(
            attrs={'class': 'state_edit'}
        )
    )

    estimate_edit = fields.DateField(
        label='Estimate',
        required=True, input_formats=['%d-%m-%Y'],
        widget=widgets.DateInput(
            attrs={'class': 'estimate_edit'}
        )
    )

    def get_data_to_edit(self):
        title = self.data.get("title_edit")
        date = self.data.get("estimate_edit")
        state = self.data.get("state_edit")
        try:
            date = datetime.strptime(date, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Incorrect data! Date should have format 'dd-mm-yyyy'")
        if date <= datetime.now().date():
            raise ValueError("Incorrect data! Date can't be less than today")
        return (title, state, date)


class DeleteForm(Form):

    title_delete = fields.CharField(
        label='Title',
        required=True, max_length=128,
        widget=widgets.Textarea(
            attrs={'class': 'title_delete'}
        )
    )

    def get_data_to_delete(self):
        title = self.data.get("title_delete")
        return (title)
