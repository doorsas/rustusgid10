from django import forms
from .models import Technika

class TechnikaForm(forms.ModelForm):
    class Meta:
        model = Technika
        fields = ('title', 'title_tag','author','body', 'operatorius','webpuslapis','epastas','nuotrauka', 'kontaktas')
        widgets = {
            'title': forms.TextInput( attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput( attrs={'class': 'form-control'}),
            'author': forms.Select( attrs={'class': 'form-control'}),
            'body': forms.TextInput( attrs={'class': 'form-control'}),
            'operatorius': forms.TextInput( attrs={'class': 'form-control'}),
            'webpuslapis': forms.URLInput(attrs={'class': 'form-control'}),
            'epastas': forms.EmailInput(attrs={'class': 'form-control'}),
            'nuotrauka': forms.ClearableFileInput(),
            'kontaktas': forms.TextInput( attrs={'class': 'form-control'}),
        }

# class EditForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'title_tag','body')
#         widgets = {
#             'title': forms.TextInput( attrs={'class': 'form-control'}),
#             'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#         }
