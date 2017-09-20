from django import forms
from .models import Input, STATES

class InputForm(forms.ModelForm):

  attrs = {'class' : 'form-control',
           'onchange' : 'this.form.submit()'}

  state = forms.ChoiceField(choices=STATES, required=True,
                            widget=forms.Select(attrs = attrs))
  class Meta:
      model = Input
      fields = ['state']
