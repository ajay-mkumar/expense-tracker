from django import forms
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password',]

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        user_name = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if not first_name:
            self.add_error('first_name', "First Name is required")
        
        if not last_name:
            self.add_error('last_name', "Last Name is required")

        return cleaned_data

            

    
