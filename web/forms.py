from django import forms
from web.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        # exclude = ("created_by", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        instance = kwargs.get("instance")