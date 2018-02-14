from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

from celery.task.schedules import crontab
from celery.decorators import periodic_task
import smtplib

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greetings.settings')
app = Celery('greetings')
app1 = Celery('contact')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@periodic_task(run_every=(crontab(minute='*/5')), name="send_msg")
# , ignore_result=True)
def send_msg():
    smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
    smtpObj.starttls()
    smtpObj.login('daisybluet@mail.ru', 'kuklamascha1988')
    smtpObj.sendmail('daisybluet@mail.ru', 'lenabelgrad@mail.ru', 'Hello from Celery!')
    smtpObj.quit()