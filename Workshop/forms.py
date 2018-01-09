from django import forms
from .models import Details

class RegisterHere(forms.ModelForm):

    Workshop = forms.MultipleChoiceField(choices=Details.WORKSHOPS, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Details

        fields = ['Name', 'Email', 'Mobile', 'Workshop']

        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'Email': forms.TextInput(attrs={'placeholder': 'Email'}),


        }
