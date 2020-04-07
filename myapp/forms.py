from django import forms

class Appform(forms.Form):

    play_app = forms.CharField(required=False)

    ios_app = forms.CharField(required=False)

    ios_app_no = forms.IntegerField(required=False)




