from django import forms
from .models import Apply, Jop


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'website', 'cv', 'cover_letter']


class JobForm(forms.ModelForm):
    class Meta:
        model = Jop
        # fields = '__all__'
        exclude = ['owner', 'job_img', 'slug']

