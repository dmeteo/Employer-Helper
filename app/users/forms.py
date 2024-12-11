from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from app.users.models import User


class UserLoginForm(forms.Form):

    class Meta:
        model = User
        fields = ('email', 'password')

    email = forms.EmailField()
    password = forms.CharField()


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "surname",
            "phone_number",
            "password1",
            "password2",
        )

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if not (phone_number.startswith('+79') or phone_number.startswith('89')):
            raise forms.ValidationError('Неверный номер телефона')
        return phone_number
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not (first_name.isalpha()):
            raise forms.ValidationError('Неверное имя')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not (last_name.isalpha()):
            raise forms.ValidationError('Неверная фамилия')
        return last_name
    
    def clean_surname(self):
        surname = self.cleaned_data['surname']
        if not (surname.isalpha()):
            raise forms.ValidationError('Неверное отчество')
        return surname
    
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    surname = forms.CharField()
    phone_number = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "surname",
            "email",
            "phone_number",
            "password")
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if not (phone_number.startswith('+79') or phone_number.startswith('89')):
            raise forms.ValidationError('Неверный номер телефона')
        return phone_number
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not (first_name.isalpha()):
            raise forms.ValidationError('Неверное имя')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not (last_name.isalpha()):
            raise forms.ValidationError('Неверная фамилия')
        return last_name
    
    def clean_surname(self):
        surname = self.cleaned_data['surname']
        if not (surname.isalpha()):
            raise forms.ValidationError('Неверное отчество')
        return surname
        

    first_name = forms.CharField()
    last_name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    password = forms.CharField()

    def get_email(self):
        return self.email
