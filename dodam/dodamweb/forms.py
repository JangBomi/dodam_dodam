from django import forms

class bookSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Book')