from django import forms
from .models import Work

class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ['img', 'type']



class UpdatePostForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ['img', 'type']

