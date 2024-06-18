from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Add new Task ...',
            'class': 'form-control'
        }),
        label='Task Title',
        max_length=200 
    )

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
