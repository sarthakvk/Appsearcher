from django import forms


class Appform(forms.Form):

    play_app = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'ex- com.appxplore.voidtroopers'}),required=False)

    ios_app = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'ex- void-troopers-sci-fi-tapper'}),required=False)

    ios_app_no = forms.IntegerField(widget= forms.TextInput(attrs={'placeholder':'ex- 1367822033'}),required=False)
