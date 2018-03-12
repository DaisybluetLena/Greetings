import random
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, request
from django.views.generic.edit import FormView, ModelFormMixin
from contact.models import AddPersonForm, AddPerson, CreateUserForm, ContactUser, LogInForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



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
        return HttpResponseRedirect('/contact/thanks/')


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonsView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return AddPerson.objects.filter(user=self.request.user)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     return context


    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     """
    #     Декорируем диспетчер функцией login_required, чтобы запретить просмотр отображения неавторизованными
    #     пользователями
    #     """
    #     return super(PersonsView, self).dispatch(request, *args, **kwargs)


class PersonDetailView(DetailView):
    model = AddPerson
    context_object_name = 'detail_view_object'
    template_name = 'contact/detail_view.html'


class LogInView(LoginView):
    model = ContactUser
    form_class = LogInForm
    template_name = 'contact/login.html'
    # redirect_field_name = '/contact/thanks'
    context_object_name = 'user'

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return HttpResponseRedirect('/contact/contacts/')
        # return super(LogInView, self).form_valid(form)


    # def form_valid(self, form):
    #     if request.user.is_authenticated():
    #         instance.user.add(request.user)

    # def get_user(self, user_id):
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None

class CreateUserView(CreateView):
    model = ContactUser
    form_class = CreateUserForm
    template_name = 'contact/registration.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/contact/thanks/')

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
