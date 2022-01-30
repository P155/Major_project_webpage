from django import forms
from .models import StudentAttend

class Student_entryForm(forms.ModelForm):
    class Meta:
        model = StudentAttend
        fields = ['first_name', 'last_name','student_name','roll_no','phone_no','email']
