from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'name': 'name',
                'placeholder': 'Your Name',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'name': 'email',
                'placeholder': 'Your Email',
                'data-rule': 'email',
                'data-msg': 'Please enter a valid email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'subject',
                'name': 'subject',
                'placeholder': 'Subject',
                'data-rule': 'minlen:4',
                'data-msg': 'Please enter at least 4 chars of subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message',
                'name': 'message',
                'rows': 12,
                'placeholder': 'Message',
                'data-rule': 'required',
                'data-msg': 'Please write something for us'
            }),
        }
