from django.forms import ModelForm
from .models import Student
from django.core.exceptions import ValidationError 

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) <3:
            raise ValidationError("Name must be at least 3 characters long.")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        existing = Student.objects.filter(email=email)
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)
        if existing.exists():
            raise ValidationError("This email is already registered.")
        return email