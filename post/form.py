from django import forms
from post.models import Comments

class FormComm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("text", "name", "email")
