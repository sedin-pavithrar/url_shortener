from django import forms

"""
Forms used in the URL shortening application.

"""


class GetUrl(forms.Form):
    """
    Form used to validate a URL submitted by the user.

    """

    original_url = forms.URLField(label="Original URL ", max_length=500)
