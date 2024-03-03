from django import forms

from .models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status']

    def clean_priority(self):
        data = self.cleaned_data['priority']
        if data < 0 or data > 5:
            raise forms.ValidationError("Priority must be between 0 and 5")
        return data