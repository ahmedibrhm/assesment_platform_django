from django.contrib import admin
   
# Register your models here.
from .models import assessment,submission
   
admin.site.register(assessment)
admin.site.register(submission)