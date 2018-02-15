from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import random
import smtplib


GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))
DEFAULT_GENDER_CHOICES = 'Укажите свой пол'
DEFAULT_L = True


class AddPerson(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=datetime.now)
    email = models.EmailField(blank=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=DEFAULT_GENDER_CHOICES)
    automatic_greeting = models.BooleanField(default=DEFAULT_L)
    user = models.ForeignKey('ContactUser', on_delete='DO_NOTHING')


class AddPersonForm(ModelForm):
    class Meta:
        model = AddPerson
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'gender', 'automatic_greeting']


class ContactUser(User):
    pass

class CreateUserForm(UserCreationForm):
# class CreateUserForm(ModelForm):
    class Meta:
        model = ContactUser
        fields = ['username', 'first_name', 'last_name', 'email']










# def make_greeting():
#     first = ["Привет! ", "Дорогой! ", "Уважаемый! "]
#     second = ["От всей души поздравляю тебя с праздником. ", "Поздравляю тебя с чудесным праздником. "]
#     third = ["С уважением, Лена", "С наилучшими пожеланиями, Лена"]
#     a = random.randint(0, len(first) - 1)
#     b = random.randint(0, len(second) - 1)
#     c = random.randint(0, len(third) - 1)
#     greeting = str(first[a] + second[b] + third[c])
#
#     return greeting
#
#
# def send_msg(email, greeting):
#     smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
#     smtpObj.starttls()
#     smtpObj.login('daisybluet@mail.ru', 'kuklamascha1988')
#     smtpObj.sendmail('daisybluet@mail.ru', email, greeting)
#     smtpObj.quit()
#
#
# def greetings():
#     contacts = AddPerson.objects.all()
#     for i in range(0, len(contacts)-1):
#         email = contacts[i].email
#         greeting = make_greeting()
#         send_msg(email, greeting)
#
# while(True):
#     greetings()



#
#
# g = 0
# contacts = AddPerson.objects.all()
# def greeting():
#     while (g != len(contacts-1):
#         for contact in contacts:
#             email = contact.email
#             if datetime.now == contact.date_of_birth:
#                 send_msg(email)
#
