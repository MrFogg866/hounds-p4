from django import forms
from django.contrib.auth.forms import UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Row, Layout, Submit
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext as _

from .models import Profile
from profiles.models import Note


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = Profile
        fields = '__all__'


class UpdateProfileForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=50,
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )
    telephone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Telephone', 'class': 'form-control'})
    )
    dog_name = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Dog Name', 'class': 'form-control'})
    )
    dog_breed = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Dog Breed', 'class': 'form-control'})
    )
    dog_allergies = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Dog Allergies', 'class': 'form-control'})
    )

    class Meta(UserChangeForm.Meta):
        model = Profile
        exclude = ['password']
        fields = ('first_name', 'last_name', 'email', 'telephone', 'dog_name', 'dog_breed', 'dog_allergies')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define crispy forms layout
        self.helper = FormHelper()
        self.helper.form_class = 'row g-3'
        self.helper.label_class = 'col-sm-2 col-form-label'
        self.helper.field_class = 'form-control'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='col-sm-6'),
                Column('last_name', css_class='col-sm-6'),
                css_class='form-row'
            ),
            Row(
                Column('email', css_class='col-sm-6'),
                Column('telephone', css_class='col-sm-6 mt-2'),
                css_class='form-row'
            ),
            Row(
                Column('dog_name', css_class='col-sm-6 mt-2'),
                Column('dog_breed', css_class='col-sm-6 mt-2'),
                css_class='form-row'
            ),
            Row(
                Column('dog_allergies', css_class='col-12 mt-1'),
            ),
            Submit('submit', 'Save', css_class='btn btn-primary w-100 mt-4')
        )


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }
