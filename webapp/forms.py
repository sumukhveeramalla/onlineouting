from tkinter.ttk import Style
from django import forms
from django.forms import ModelForm
from .models import student


class studentForm(ModelForm):
    class Meta:
        model = student
        fields = ('name','rollnumber','description','prefer','Residence','year','phoneNo')
        
        widgets = {
            'name' : forms.TextInput(attrs={'style': 'width:50%','style':'text-align: center', 'Style' : 'vertical-align:middle','placeholder':'Name'}),
            'rollnumber': forms.NumberInput(attrs={'placeholder':'Roll Number:'}),
            'description':forms.TextInput(attrs={'placeholder':'Reason'}),
            'prefer':forms.TextInput(attrs={'placeholder':'Local OR Non Local'}),
            'Residence':forms.TextInput(attrs={'placeholder':'Hostel Block'}),
            'year':forms.TextInput(attrs={'placeholder':'Year Studying'}),
            'phoneNo':forms.TextInput(attrs={'placeholder':'Phone Number'})
        }

class studentFormOne(ModelForm):
    class Meta:
        model = student
        fields = ('__all__')
        widgets = {
            'name' : forms.TextInput(attrs={'style': 'width:50%','style':'text-align: center', 'Style' : 'vertical-align:middle','placeholder':'Name'}),
            'rollnumber': forms.NumberInput(attrs={'placeholder':'Roll Number:'}),
            'description':forms.TextInput(attrs={'placeholder':'Reason'}),
            'prefer':forms.TextInput(attrs={'placeholder':'Local OR Non Local'}),
            'Residence':forms.TextInput(attrs={'placeholder':'Hostel Block'}),
            'year':forms.TextInput(attrs={'placeholder':'Year Studying'}),
            'phoneNo':forms.TextInput(attrs={'placeholder':'Phone Number'}),
            'status':forms.TextInput(attrs={'placeholder':'yes or no'})
        }
