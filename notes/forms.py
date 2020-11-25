from django import forms
from notes.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        #fields = ['name', 'contact', 'email'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/

        fields = ['name', 'contact'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
        #    'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.Textarea(attrs={ 'class': 'form-control' }),
      }
