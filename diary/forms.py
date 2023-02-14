from django import forms
from .models import Day

# class DayCreateForm(forms.ModelForm):

#     class Meta:
#         model=Day
#         fields="__all__"
        
class NippoModelForm(forms.ModelForm):
    class Meta:
        model=Day
        fields="__all__"
        widgets = {
    "title": forms.TextInput(attrs={"placeholder":"タイトル..."}),
    "text": forms.Textarea(attrs={"placeholder":"内容..."})
    }
        

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs.update({"class":"form-control"})
        super().__init__(*args, **kwargs)
