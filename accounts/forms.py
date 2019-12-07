from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


def check(email):
    if "@gmail.com" in email or "@kiit.ac.in" in email:
        return True
    return False


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control cusinput", "placeholder": "Email/Username"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control cusinput", "placeholder": "Password"}))


class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control cusinput", "placeholder": "Full name"}))
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
        if check(email):
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("Account with the same email already exists!")
            return email
        else:
            raise forms.ValidationError("Invalid email, please use Gmail or Kiitmail!")

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords don't match!")
        return password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must contain more than 8 characters!")
