from django import forms
from django.forms import ModelForm
from .models import student


class studentForm(ModelForm):
    class Meta:
        model = student
        fields = ('name','rollnumber','description','prefer','Residence','year','phoneNo')
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'rollnumber': forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'prefer':forms.TextInput(attrs={'class':'form-control'}),
            'Residence':forms.TextInput(attrs={'class':'form-control'}),
            'year':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNo':forms.TextInput(attrs={'class':'form-control'})
        }

class studentFormOne(ModelForm):
    class Meta:
        model = student
        fields = ('__all__')
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'rollnumber': forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'prefer':forms.TextInput(attrs={'class':'form-control'}),
            'Residence':forms.TextInput(attrs={'class':'form-control'}),
            'year':forms.TextInput(attrs={'class':'form-control'}),
            'phoneNo':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.TextInput(attrs={'class':'form-control'})
        }
