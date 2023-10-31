#django forms for input.
from django import forms

class JumpForm(forms.Form):
    jumps = forms.IntegerField(
        label='Preferred number of character jumps',
        min_value=1,
        max_value=26
    )
