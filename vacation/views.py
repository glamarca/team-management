from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from vacation.models import Vacation, Demand, Task, DemandStatus, Person


def page_not_found(request):
    return render(request,'page_not_found.html')

def access_denied(request):
    return render(request,'acces_denied.html')

@login_required
def home(request):
    person = Person.objects.get(username=request.user)
    vacations = Vacation.objects.filter(person=person)
    last_demands = DemandStatus.objects.filter(person = person)[0:5]
    tasks = Task.objects.filter(person=person)
    context = {
        'vacations' : vacations,
        'last_demands' : last_demands,
        'person' : person,
        'tasks' : tasks
    }
    return render(request, "home.html",context)