from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})