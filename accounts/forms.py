from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django import forms
from blogweb.models import ProfileUser


# Registration form
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2'
        )
        help_texts = {
            'username': 'Username must contain atleast 8 Characters',

            'password2': 'Confirmation Password'
        }
        error_messages = {
            'username': {
                'required': "Your name must be atleast 8 character"
            }
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Fullname',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter e-mail address'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    # validates a data from a form for registration
    def clean(self):
        super(UserForm, self).clean()

        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if len(username) < 6:
            self._errors['username'] = self.error_class([
                'Minimum 6 characters required'])

        if len(password1) < 8:
            self._errors['password1'] = self.error_class(["Password must contain atleast 8 characters"])

        if password1 != password2:
            self._errors['password2'] = self.error_class(['Password didnot match'])

        return self.cleaned_data


# specific user creation form
class ProfileCreateFrom(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = (
            'bio', 'website_url', 'facebook_url', 'instagram_url', 'linkedIn_url'
        )
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',

            }),
            'website_url': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'facebook_url': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'instagram_url': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'linkedIn_url': forms.TextInput(attrs={
                'class': 'form-control',

            }),

        }


# specific user profile edit form
class ProfileEditView(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'last_login',
            'date_joined'
        )

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter firstname',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter lastname',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',

            }),
            'last_login': forms.DateTimeInput(format="%Y-%m-%d %H:%M", attrs={
                'class': 'form-control',
                'readonly': 'True'
            }),

            'date_joined': forms.DateTimeInput(format="%m/%d/%Y", attrs={
                'class': 'form-control',
                'readonly': 'True'
            }),

        }
