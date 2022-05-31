from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from .models import submission, assessment


class AssessmentForm(ModelForm):
    class Meta:
        model = assessment
        fields = ['Title','Description','Deadline']


class SubmissionForm(ModelForm):
    class Meta:
        model = submission
        fields = ['StudentName','File', 'Link','Assessment']
class Grading(ModelForm):
    class Meta:
        model = submission
        fields = ['Grade', 'Remark']
"""
class SubmissionForm(forms.Form):
    StudentName = forms.CharField(max_length=200)
    File = forms.FileField(required=False)
    Link = forms.URLField(required=False)
    DateOfSubmission = forms.DateField()
    def clean_renewal_date(self):
        data = self.cleaned_data['DateOfSubmission']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - Submission in past'))

        # Remember to always return the cleaned data.
        return data
"""