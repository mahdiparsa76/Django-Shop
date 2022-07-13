from django import forms
from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': 'message'
            })
        }

        labels = {
            'full_name': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما'
        }

        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'
            }
        }
