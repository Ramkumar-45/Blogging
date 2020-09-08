from django import forms
from .models import Post

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


# Post form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'title_tag', 'author', 'body'
        )

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'user',
                'type': 'hidden'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',

            }),

        }


# class for editing posts
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'title_tag', 'body'
        )


# contact for mail to admin
class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(ContactForm, self).__init__(*args, **kwargs)
