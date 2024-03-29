from django import forms 
from .models import AddTutors ,Review
class AddTutorForm(forms.ModelForm):
    class Meta:
        model =AddTutors
        fields ="__all__"
        
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =['name','email','rating','body']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name '}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email '}),
            
            'body': forms.Textarea(attrs={'placeholder': 'Tell us about yourself'}),
            
        }