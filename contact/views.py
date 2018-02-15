import random
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView, ModelFormMixin
from contact.models import AddPersonForm, AddPerson, CreateUserForm, ContactUser
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



def thanks(request):
    return render(request, 'contact/thanks.html')


def changed(request):
    return render(request, 'contact/changed.html')


class AddPersonView(CreateView):
    template_name = 'contact/add.html'
    model = AddPerson
    form_class = AddPersonForm
    # success_url = 'contact/thanks.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/contact/thanks')


class AddPersonUpdate(UpdateView):
    context_object_name = 'person_update'
    template_name = 'contact/change.html'
    # template_name_suffix = 'add_person/change.html'
    model = AddPerson
    form_class = AddPersonForm
    # success_url = 'contact/changed.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/contact/changed')


def hello(request):
    return render(request, 'contact/hello.html')


class PersonsView(ListView):
    model = AddPerson

    template_name = 'contact/contacts.html'


class PersonDetailView(DetailView):
    model = AddPerson
    context_object_name = 'detail_view_object'
    template_name = 'contact/detail_view.html'


# def hello(request):
#     if request.method == 'POST':
#         f = UserCreationForm(request.POST)
#         if f.is_valid():
#             f.save()
#             # messages.success(request, 'Account created successfully')
#             return HttpResponseRedirect('/contact/thanks')
#
#     else:
#         f = UserCreationForm()
#
#     return render(request, 'contact/hello.html', {'form': f})


class CreateUserView(CreateView):
    model = ContactUser
    form_class = CreateUserForm
    template_name = 'contact/registration.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/contact/thanks')

#рабочий вариант

# def add_person(request):
#     form = AddPersonForm(request.POST)
#     if request.method == 'POST':
#         form = AddPersonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'add_person/thanks.html')
#         else:
#             form = AddPersonForm()
#
#     return render(request, 'add_person/add_person.html', {'form': form})
