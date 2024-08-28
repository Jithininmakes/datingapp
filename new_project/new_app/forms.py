from django import forms
from django.core.exceptions import ValidationError

from .models import User, WorkLocation, Designation, Hobby
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User, Interest


class RegisterForm (forms.ModelForm):

    class Meta:
        model = User
        fields = ["age","dob","hobbies","interest","drinking_habits",
                  "smoking_habits","qualification","profile_picture","multiple_image","short_reel"]
        widgets = {
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age',
            }),

            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'type':'date',
                'placeholder': 'DOB',
            }),
            'hobbies': forms.Select(attrs={
                'class': 'form-control',
            }),

            'interest': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ' Interests',
            }),
            'drinking_habits': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Drinking Habit'
            }),
            'smoking_habits': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Smoking Habit'
            }),

            'qualification': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ' Qualification',
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #ced4da; padding: 10px;',
                'title': 'Upload Profile Picture',
            }),
            'multiple_image': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #ced4da; padding: 10px;',
                'title': 'Upload Profile Picture',

            }),
            'short_reel': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #ced4da; padding: 10px;',
            }),
        }

        labels = {
            'age': '',
            'dob': ' ',
            'hobbies': ' ',
            'interest': '',
            'drinking_habits': ' ',
            'smoking_habits': '',
            'qualification': ' ',
            'profile_picture': '',
            'multiple_image': ' ',
            'short_reel': ' ',

        }

        error_messages = {
            'age': {
                'required': '',
            },
            'dob': {
                'required': '',
            },
            'hobbies': {
                'required': '',
            },
            'interest': {
                'required': '',
            },
            'drinking_habits': {
                'required': '',
            },
            'smoking_habits': {
                'required': '',
            },
            'qualification': {
                'required': '',
            }
        }


    def __init__(self, *args, **kwargs):
       super(RegisterForm, self).__init__(*args, **kwargs)
       self.fields['hobbies'].empty_label = "Hobby"
       self.fields['interest'].empty_label = "Interest"
       self.fields['qualification'].empty_label = "Qualification"



class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = ['name']

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['name']

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['name']

class WorkLocationForm(forms.ModelForm):
    class Meta:
        model = WorkLocation
        fields = ['name']




class EmployerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['company_name','designation','work_location']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' Company Name',
            }),

            'designation': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ' Designation',
            }),
            'work_location': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ' Work Location',
            }),
        }

        labels = {
            'company_name': '',
            'designation': ' ',
            'work_location': ' ',
        }
    def __init__(self, *args, **kwargs):
       super(EmployerForm, self).__init__(*args, **kwargs)
       self.fields['company_name'].empty_label = "Company Name"
       self.fields['designation'].empty_label = "Designation"
       self.fields['work_location'].empty_label = "Work Location"