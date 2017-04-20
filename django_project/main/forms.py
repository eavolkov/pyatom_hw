from django.forms import Form, fields, widgets
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta, date

class CreateForm(Form):

    title = fields.CharField(
        label='Заголовок',
        required=True, max_length=128,
        widget=widgets.Textarea(
            attrs={'class': 'title'}
        )
    )

    estimate = fields.DateField(
        label='Срок выполнения',
        required=True, input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'],
        widget=widgets.DateInput(
            attrs={'class': 'estimate'}
        )
    )

    def clean_title(self):
        value = self.cleaned_data.get('title')
        #if not value.startswith('Привет,'):
        #     raise ValidationError('Сообщение должно начинаться с приветствия!')
        return value

    def clean_estimate(self):
        value = self.cleaned_data.get('estimate')
        #if not value.startswith('Привет,'):
        #    raise ValidationError('Сообщение должно начинаться с приветствия!')
        return value
