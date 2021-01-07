from django import forms
from .models import Comment




class AddReplyForm(forms.ModelForm):
      class Meta:
        model=Comment
        fields=('body',)