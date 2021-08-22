from django import forms

from .models import Member


class MemberModelForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'name',
            'tc',
            'phone',
            'address',
        ]
    
    