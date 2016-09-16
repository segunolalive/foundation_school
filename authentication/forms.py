from django import forms
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField

from .models import Account

# class LoginForm(AuthenticationForm):
class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=255,
            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))
    password = forms.CharField(label="Password", max_length=30,
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class ContactForm(forms.Form):
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=80, required=False)
    last_name = forms.CharField(max_length=80, required=False)
    message = forms.CharField(widget=forms.Textarea)


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password. The name is in line with Django Presets"""
    email = forms.CharField(label='Email',
            widget=forms.EmailInput(attrs={'class': 'form-control',
            'name': 'email'}))
    first_name = forms.CharField(label='first_name',
                widget=forms.TextInput(attrs={'class': 'form-control',
                'name': 'first_name'}))
    password1 = forms.CharField(label='Password',
                widget=forms.PasswordInput(attrs={'class': 'form-control',
                'name': 'password1'}))
    password2 = forms.CharField(label='Password confirmation',
                 widget=forms.PasswordInput(attrs={'class': 'form-control',
                 'name': 'password2'}))

    class Meta:
        model = Account
        fields = ('email', 'first_name')

    def clean_password2(self):
    # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        account = super(UserCreationForm, self).save(commit=False)
        account.set_password(self.cleaned_data["password1"])
        if commit:
            account.save()
        return account


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field. The name is in line with Django Presets
    """
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = Account
        fields = ('email', 'password', 'first_name', 'is_active', 'is_admin')

    def clean_password(self):
    # Regardless of what the user provides, return the initial value.
    # This is done here, rather than on the field, because the
    # field does not have access to the initial value
        return self.initial["password"]
