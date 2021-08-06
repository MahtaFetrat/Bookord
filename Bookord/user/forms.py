from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='your name', max_length=100)

    #hleft from here : https://docs.djangoproject.com/en/3.1/topics/forms/#the-view