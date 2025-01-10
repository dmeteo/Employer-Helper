from django import forms
from app.tasks.models import Task


class TaskForm(forms.ModelForm):

    class Meta():
        model = Task
        fields = (  
                    'date_start',
                    'deadline',
                    'title',
                    'description',
                    'requirments',
                  )

        
    date_start = forms.DateField()
    deadline = forms.DateField()
    title = forms.CharField()
    description = forms.CharField()
    requirments = forms.CharField()

        
    