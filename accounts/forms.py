from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):  # SignupFormを継承する
    last_name = forms.CharField(max_length=30, label='名字')
    first_name = forms.CharField(max_length=30, label='名前')
    company_name = forms.CharField(max_length=100, label='会社名')
    company_address = forms.CharField(max_length=100, label='会社住所')
    tel_number = forms.CharField(max_length=15, label="携帯電話番号（ハイフンあり）")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.company_name = self.cleaned_data['company_name']
        user.company_address = self.cleaned_data['company_address']
        user.tel_number = self.cleaned_data['tel_number']
        user.save()
        return user