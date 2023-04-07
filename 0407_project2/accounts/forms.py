from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            attrs={
                'type':'date',
                'class': 'form-control mt-2 mb-3',
            }
        ),
        required=False,
    )

    username = forms.CharField(
        label='아이디',
         widget=forms.DateInput(
            attrs={
                'class': 'form-control mt-2 mb-3',
            }
        )
    )

    email = forms.CharField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'type':'email',
                'class': 'form-control mt-2 mb-3',
            }
        ),
        required=False,
    )

    first_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mt-2 mb-3',
            }
        ),
        required=False,

    )

    last_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mt-2 mb-3',
            }
        ),
        required=False,
    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'class': 'form-control mt-2 mb-3',
            }
        )
    )

    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'type':'password',
                'class': 'form-control mt-2 mb-3',
            }
        )
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'password1', 'password2')



class CustomUserChangeForm(UserChangeForm):
    birthday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            attrs={
                'type':'date',
                'class': 'form-control mt-2 mb-3',
            }
        ),
        required=False,
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'birthday')