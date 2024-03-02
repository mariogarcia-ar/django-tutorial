from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField( max_length=200)
    description = forms.CharField(widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField( max_length=200)
