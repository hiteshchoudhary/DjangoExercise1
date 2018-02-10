from django import forms


class VideoForm(forms.Form):
    videoname = forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name',
        'id': 'inputName'
        }))
    videodesc = forms.CharField(widget=forms.Textarea({
        'class': 'form-control',
        'rows': '5',
        'id': 'comment',
        'placeholder': 'Comment'
        }))
