from django import forms
from django.contrib.auth.forms import UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Profile
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label='Password',
        help_text='Raw passwords are not stored, so there is no way to see this user’s password, but you can change the password using <a href="./password/">this form</a>.',
    )

    class Meta(UserChangeForm.Meta):
        model = Profile
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the password field from the form
        del self.fields['password']
        # Remove the username field from the form


class UpdateProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Profile
        exclude = ['password']
        fields = ('first_name', 'last_name', 'email', 'bio', 'location')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add form helper
        self.helper = FormHelper()
        self.helper.form_class = 'row g-3'
        self.helper.label_class = 'col-sm-2 col-form-label'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary w-100'))

        # Add Bootstrap 5 classes and placeholder text to fields
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': field.label})

        # Set default email value
        self.fields['email'].initial = self.instance.email or self.Meta.model._meta.get_field('email').get_default()

    def clean_email(self):
        # Get the current email value
        return self.instance.email
