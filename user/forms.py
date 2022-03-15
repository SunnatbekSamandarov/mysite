from django import forms
from .models import Contact

class UserForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['Name','Email','Project','Message']

        def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)

        def save(self, commit=True):
            instance = super(UserForm, self).save(commit=False)
            if commit:
                instance.save()
            return instance



