from django import forms
from .models import Post, Comment, Attachment
from multiupload.fields import MultiFileField

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'video')

    files = MultiFileField(min_num=0, max_num=10, max_file_size=1024*1024*5, required=False)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

    files = MultiFileField(min_num=1, max_num=1, max_file_size=1024*1024*5, required=False)
