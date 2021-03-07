from django import forms
from .models import Technika
from accounts.models  import CustomUser

class TechnikaForm(forms.ModelForm):
    class Meta:
        model = Technika
        fields = ('title', 'title_tag','author','body', 'operatorius','webpuslapis','epastas','nuotrauka', 'kontaktas')
        widgets = {
            'title': forms.TextInput( attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput( attrs={'class': 'form-control'}),
<<<<<<< HEAD
            'author': forms.Select (attrs={'class': 'form-control'}),
            'body': forms.Textarea( attrs={'class': 'form-control'}),
            'operatorius': forms.CheckboxInput( attrs={'class': 'form-control'}),
            'webpuslapis': forms.URLInput( attrs={'class': 'form-control'}),
=======
            'author': forms.Select( attrs={'class': 'form-control'}),
            'body': forms.TextInput( attrs={'class': 'form-control'}),
            'operatorius': forms.TextInput( attrs={'class': 'form-control'}),
            'webpuslapis': forms.URLInput(attrs={'class': 'form-control'}),
>>>>>>> fae690f7f52be2d23b7c830fab17e71186b382c5
            'epastas': forms.EmailInput(attrs={'class': 'form-control'}),

            'kontaktas': forms.TextInput( attrs={'class': 'form-control'}),
        }

class EditTechnika(forms.ModelForm):
    class Meta:
        model = Technika
        fields = ('title', 'title_tag','author','body', 'operatorius','webpuslapis','epastas','nuotrauka', 'kontaktas')
        widgets = {
            'title': forms.TextInput( attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput( attrs={'class': 'form-control'}),
            'author': forms.Select (attrs={'class': 'form-control'}),
            'body': forms.Textarea( attrs={'class': 'form-control'}),
            'operatorius': forms.CheckboxInput( attrs={'class': 'form-control'}),
            'webpuslapis': forms.URLInput( attrs={'class': 'form-control'}),
            'epastas': forms.EmailInput(attrs={'class': 'form-control'}),

            'kontaktas': forms.TextInput( attrs={'class': 'form-control'}),
        }

