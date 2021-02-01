from django import forms
from django.core import validators

class UserForm(forms.Form):
    first_name=forms.CharField(validators=[validators.MaxLengthValidator(15),validators.MinLengthValidator(5)],label="First Name",initial="please Enter your name")
    last_name=forms.CharField(max_length=100,label="Last Name",initial="please Enter your name",required=True)
    choicefield=forms.ChoiceField(choices=((1,"good"),(2,"better")))
    boolean=forms.BooleanField()
    email=forms.EmailField()
    vmail=forms.EmailField()

    def clean(self):
        get_context_data=super().clean()
        email=get_context_data["email"]
        vmail=get_context_data["vmail"]

        if email!=vmail:
            raise forms.ValidationError("Email Not Matched")
