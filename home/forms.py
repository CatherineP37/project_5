from django import forms
from django.forms import ModelForm
from .models import Contact, Attendance


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"
      