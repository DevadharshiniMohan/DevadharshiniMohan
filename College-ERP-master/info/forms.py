from django import forms
from django.forms import ModelForm
from .models import Office_staff
from crispy_forms.helper import FormHelper



class Office_staff_form(ModelForm):
    class Meta:

        model = Office_staff
        
        fields = ('ID','Name', 'Sex', 'DOB', 'Skills', 'Designation')

        widgets = {
            'Name': forms.TextInput(attrs={'class':'input lg','style': 'width: 300px;'}),
            'Sex' : forms.RadioSelect(attrs={'required':'False'}),
            'DOB' : forms.TextInput(attrs={'type':'date','style': 'width: 300px;'}),
            'Designation': forms.Select(attrs={'style': 'width: 300px;'}),
        }
       

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper = FormHelper(self)
            



            
        
