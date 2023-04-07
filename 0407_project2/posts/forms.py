from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    CHOICES = [('개발', '개발'), ('CS', 'CS'), ('신기술', '신기술')]
    category = forms.ChoiceField(
        widget = forms.Select(
            attrs = {
                'class': 'form-select mt-2',
            }
        ), 
        choices=CHOICES)
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'category')