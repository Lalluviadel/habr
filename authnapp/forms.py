from django.contrib.auth.forms import AuthenticationForm
from userapp.models import HabrUser


class HabrUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(HabrUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = HabrUser
        fields = ("username", "password")
