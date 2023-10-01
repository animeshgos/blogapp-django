from django import forms

from .models import Post

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('tag', 'name', 'content', 'image',)
        widgets = {
            'tag': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'content', 'image')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
