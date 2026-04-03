from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

# In django forms are created dyamically by referring the models schema and create its own form using Meta forms.

# So easy to implement the forms in Django, no need to do it manually.

# Create Forms -> Models -> Dynamic Form created