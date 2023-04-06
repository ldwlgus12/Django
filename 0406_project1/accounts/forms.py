from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            attrs={
                'type':'date',
            }
        )
    )

    username = forms.CharField(
        label='아이디',

    )

    email = forms.CharField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'type':'email',
            }
        )
    )

    first_name = forms.CharField(
        label='성',

    )

    last_name = forms.CharField(
        label='이름',

    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.TextInput(
            attrs={
                'type':'password',
            }
        )
    )

    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.TextInput(
            attrs={
                'type':'password',
            }
        )
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'password1', 'password2')



class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')