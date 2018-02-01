from django.db import models
from django.forms import ModelForm


class AddPerson(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()


class AddPersonForm(ModelForm):
    class Meta:
        model = AddPerson
        fields = ['first_name', 'last_name', 'email']
