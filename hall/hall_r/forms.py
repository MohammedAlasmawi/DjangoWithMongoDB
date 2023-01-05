from django import forms
from .models import Hall


class HallForm(forms.ModelForm):

    class Meta:
        model = Hall
        fields = ('Name','Size','Location','Description')

        labels = {
            'Name':'Name',
            'Size':'Size'
        }

    def __init__(self, *args, **kwargs):
        super(HallForm,self).__init__(*args, **kwargs)
        self.fields['Size'].required = False
