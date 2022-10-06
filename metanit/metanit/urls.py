from django.urls import path
from hello import views

urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
    path("about/", views.about),
    path("contacts/", views.contacts),
    path("narod/", views.narod),

]