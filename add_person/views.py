from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from add_person.models import AddPersonForm


class AddPersonView(FormView):
    template_name = 'add_person/add_person.html'
    form_class = AddPersonForm
    success_url = 'thanks'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())


def thanks(request):
    return render(request, 'add_person/thanks.html')




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
