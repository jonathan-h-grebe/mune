from django import forms
from web.models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'
        # exclude = ("created_by", )

        error_messages = {
            'tel_number': {
                'required': '必須です!',
            },
            'username': {
                'max_length': '長いです',
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tel_number"].required = True
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        instance = kwargs.get("instance")
