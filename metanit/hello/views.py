from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person, Cbr_data


def contacts(request):
    return render(request, "contacts.html")

def narod(request):
    people = Person.objects.all()
    return render(request, "narod.html", {"people": people})

def cbr(request):
    money = Cbr_data.objects.all()
    return render(request, "cbr.html", {"money": money})

def about(request):
    return render(request, "about.html")


# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})
    #return render(request, "index.html")


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")