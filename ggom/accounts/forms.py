from django import forms
from .models import CustomUser

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image']

class ChangeNicknameForm(forms.Form):
    new_nickname = forms.CharField(max_length=50, label='new_nickname')