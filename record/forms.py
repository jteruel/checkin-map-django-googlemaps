from django import forms 

from .models import Record

class RecordForm(forms.ModelForm):
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required =True)
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required = True)
    class Meta:
        model = Record
        fields = [
            "location","text",
            ]