from django import forms 

class GetUrl(forms.Form):
    original_url = forms.URLField(
        label = "Original URL ",
        max_length= 500 
    )