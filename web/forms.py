from django import forms
from web.models import Item, Case
from django.core.exceptions import ValidationError


class ItemForm(forms.ModelForm):
    # CHOICES = ((k, k) for k in ("SONY", "HITACHI", "MITSUBISHI"))
    # maker = forms.ChoiceField(choices=CHOICES, label="メーカー")
    class Meta:
        model = Item
        exclude = ("price_type", "status")

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
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    # def clean_model_year(self):
    #     data = self.cleaned_data['model_year']
    #     print(data)
    #     if not data:
    #         raise ValidationError("年式を入れてください")
    #     return data


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'case_type', "memo",
            "item_list",
            "user_name", "mail_address", "tel_number", "company_name", "company_address",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



