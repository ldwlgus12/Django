from django import forms
from .models import Article


# class AritlcleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


class AritlcleForm(forms.ModelForm):
    # inner class? 개념? 파이썬 문법과 아무런 상관없고
    # 그냥 django ModelForm의 구조가 이렇게 설계되었을 뿐

    class AritlcleForm(forms.Form):
        title = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'my-title',
                }
            )
        )

    # ModelForm의 정보를 작성하는 곳
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)