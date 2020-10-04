from django import forms
from .models import Movies,Crew,Banner_images
class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = [
            'comming_soon',
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

class Banner_imagesForm(forms.ModelForm):
    class Meta:
        model = Banner_images
        fields = [
            'banner_image1',
            'banner_image1_link',
            'banner_image2',
            'banner_image2_link',
            'banner_image3',
            'banner_image3_link',
        ]
        widgets = {
            "banner_image1_link": forms.TextInput(attrs={'class':'form-control'}),
            "banner_image2_link": forms.TextInput(attrs={'class':'form-control'}),
            "banner_image3_link": forms.TextInput(attrs={'class':'form-control'}),
        }