# app - forms.py file new
from django import forms
from .models import User

print(User)
print(User._meta.fields)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "name",
            "photo",
            "email",
            "password",
            "mobile_number",
            "date_of_birth",
        )
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
