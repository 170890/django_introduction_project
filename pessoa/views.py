from django.http import HttpResponse,Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Contact, People
from .forms import FormPeople, FormContact

class PeopleViewList(ListView):
    model = People
    queryset = People.objects.all().order_by('full_name')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        name_filter = self.request.GET.get('name') or None

        if name_filter:
            queryset = queryset.filter(full_name__contains=name_filter)
        return queryset

class CreatePeopleView(CreateView):
    model = People
    form_class = FormPeople
    success_url = '/people/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdatePeopleView(UpdateView):
    model = People
    form_class = FormPeople
    success_url = '/people/'

class DeletePeopleView(DeleteView):
    model = People
    success_url = '/people/'

def contacts(request, pk_people):
    contacts = Contact.objects.filter(people=pk_people)
    return render(request, 'contact/contact_list.html', {'contacts': contacts, 'pk_people': pk_people})

def new_contact(request, pk_people):
    form = FormContact()
    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.people_id = pk_people;
            contact.save()
            return redirect(reverse('people.contacts', args=[pk_people]))
    return render(request, 'contact/contact_form.html', {'form': form})

def update_contact(request, pk_people, pk):
    contact = get_object_or_404(Contact, pk=pk)
    form = FormContact()
    if request.method == 'POST':
        form = FormContact(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(reverse('people.contacts', args=[pk_people]))

    return render(request, 'contact/contact_form.html', {'form': form})

def delete_contact(request, pk_people, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect(reverse('people.contacts', args=[pk_people]))
