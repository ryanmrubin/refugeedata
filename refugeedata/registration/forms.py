import django.forms as forms

from refugeedata.models import Person


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
            "name",
            "preferred_lang",
            "needs",
            "email",
            "phone",
            "preferred_contact",
        ]

    def clean_preferred_contact(self):
        field_name = "preferred_contact"
        preferred_contact = self.cleaned_data[field_name]
        if preferred_contact == "P":
            self.cleaned_data["phone_preferred"] = True
        elif preferred_contact == "E":
            self.cleaned_data["email_preferred"] = True
        return preferred_contact

    def clean(self):
        data = self.cleaned_data
        if data.get("email_preferred", False) and not data.get("email"):
            error = self.fields["email"].default_error_messages["required"]
            self.add_error("email", error)
        if data.get("phone_preferred", False) and not data.get("phone"):
            error = self.fields["phone"].default_error_messages["required"]
            self.add_error("phone", error)
        return data