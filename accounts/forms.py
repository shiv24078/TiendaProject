from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1"]

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password != password2:
            self.add_error('password2', 'La contraseñas no conciden')
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "address", "card_number", "card_expiry", "card_cvv"]
