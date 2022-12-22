from django import forms
from .models import IndustryType, Company



class IndustryTypeForm(forms.ModelForm):
    class Meta:
        model = IndustryType
        fields = [
            "name",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})




class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "company_name",
            "owner_name",
            "address",
            "email",
            "contact",
            "industry_type"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})