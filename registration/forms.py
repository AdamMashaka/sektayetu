from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['entry_category', 'firstname', 'middlename', 'surname', 'sex', 'country_of_citizenship', 'birthdate', 'phone']
