from django import forms


class MyForm(forms.Form):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    username = forms.CharField(max_length=20)
