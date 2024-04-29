from django import forms
from django.forms import ModelForm
from .models import Contact, Attendance


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets={
            'name' : forms.TextInput(attrs={'style': "width:100%;"}),
            'email' : forms.TextInput(attrs={'style': "width:100%;"}),
            'message' : forms.Textarea(attrs={'style': "width:100%;"}),
        }

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"
       
      