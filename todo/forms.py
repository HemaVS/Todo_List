from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control description-box',
                'placeholder': 'Describe your task here...',
                'style': 'border: 2px dashed #0066ff; height: 150px; padding: 10px;',
            }),
        }