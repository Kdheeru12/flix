from django import forms
from .models import Movies,Crew
class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = [
            'title',
            'plot',
            'thumbnail_image',
            'banner_image',
            'upload_video',
            'price',
            'language',
            'genre',
            'age_restrication',
            'parental_guidance',
        ]
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
            'plot': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'language':forms.Select(attrs={'class':'form-control'}),
            'age_restrication':forms.Select(attrs={'class':'form-control'}),    
        }
class CrewFrom(forms.ModelForm):
    class Meta:
        model = Crew
        fields = [
            'name',
            'photo',
            'role',
            'about',
        ]
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control'}),
            "role": forms.TextInput(attrs={'class':'form-control'}),
            "about": forms.Textarea(attrs={'class':'form-control'}),
        }