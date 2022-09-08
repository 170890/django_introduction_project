from django.urls import path
from django.contrib.auth.decorators import login_required
from.views import PeopleViewList, CreatePeopleView, UpdatePeopleView, DeletePeopleView
from . import views

urlpatterns = [
    path('', login_required(PeopleViewList.as_view()), name='people.index'),
    path('new/', login_required(CreatePeopleView.as_view()), name='people.new'),
    path('<int:pk>/update', login_required(UpdatePeopleView.as_view()), name='people.update'),
    path('<int:pk>/delete',login_required(DeletePeopleView.as_view()), name='people.delete'),
    path('<int:pk_people>/contacts', login_required(views.contacts), name='people.contacts'),
    path('<int:pk_people>/contact/new/', login_required(views.new_contact), name='contact.new'),
    path('<int:pk_people>/contact/<int:pk>/update', login_required(views.update_contact), name='contact.update'),
    path('<int:pk_people>/contact/<int:pk>/delete', login_required(views.delete_contact), name='contact.delete')
]