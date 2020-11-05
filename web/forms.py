from django import forms
from web.models import Item, Case
from django.core.exceptions import ValidationError


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
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        instance = kwargs.get("instance")

    def clean_model_year(self):
        data = self.cleaned_data['model_year']
        print(data)
        if True:
            raise ValidationError("年式を入れてください")
        raise ValidationError("年式を入れてください")
        return data


class CaseForm(forms.ModelForm):
    # CHOICES = (("A", "A"), ("AB", "AB"))
    # item_id_list = forms.MultipleHiddenInput()

    class Meta:
        model = Case
        fields = [
            'case_type', "memo",
            "item_list",
            "user_name", "mail_address", "tel_number", "company_name", "company_address",
        ]
        # widgets = {"item_list": forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        # item_list = (i.id for i in kwargs['initial']['item_list'])
        # self.fields['item_list'].queryset = Item.objects.filter(id__in=item_list)



