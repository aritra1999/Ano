from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control cusinput", "placeholder": "Email/Username"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control cusinput", "placeholder": "Password"}))


class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control cusinput", "placeholder": "Username"}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control cusinput", "placeholder": "Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control cusinput", "placeholder": "Email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control cusinput", "placeholder": "Password"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={"class": "form-control cusinput", "placeholder": "Confirm Password"}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Account with the same email already exists!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Two Passwords don't match!")
        return data