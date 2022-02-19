from django import forms

class RulesForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    rules = forms.CharField(widget=forms.Textarea)