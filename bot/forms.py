from django import forms
from .models import Clickboard


# creating a form
class ClickboardForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Clickboard

        # specify fields to be used
        fields = [
            # don't forget to add "author"
            #"create_date",
            "name",
            "commands",
        ]