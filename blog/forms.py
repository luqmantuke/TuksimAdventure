from django import forms 
from blog.models import Post
from ckeditor.widgets import CKEditorWidget
 
class PostForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput())
    # image = forms.FileField(widget=forms.FileInput)
    # body = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = Post
        fields = ('name', 'image', 'body')