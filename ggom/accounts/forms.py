from django import forms
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext as _


class ProfileImageForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'style': 'display: none;'}))
    class Meta:
        model = CustomUser
        fields = ['profile_image']


class ChangeNicknameForm(forms.Form):
    new_nickname = forms.CharField(max_length=50)


'''
class CustomPasswordChangeForm(PasswordChangeForm):
    error_messages = {
        'password_incorrect': _("입력한 기존 비밀번호가 올바르지 않습니다."),
        'password_mismatch': _("입력한 새 비밀번호가 일치하지 않습니다."),
        'password_minimum_length': _("비밀번호는 최소 8자 이상이어야 합니다."),
        'password_alphanumeric': _("비밀번호는 알파벳 대문자 및 소문자를 포함하고, 최소 1개 이상의 숫자를 포함해야 합니다."),
    }

    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')
        if len(password) < 8:
            raise forms.ValidationError(self.error_messages['password_minimum_length'])
        if not (any(char.isdigit() for char in password) and (any(char.isalpha() for char in password))):
            raise forms.ValidationError(self.error_messages['password_alphanumeric'])
        return password

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'])

'''
