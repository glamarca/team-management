from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from vacation.models import Vacation, Demand, Task, DemandStatus, Person, AccountStatus
from django.utils.translation import ugettext as _


def page_not_found(request):
    return render(request,'page_not_found.html')

def access_denied(request):
    return render(request,'acces_denied.html')

@login_required
def home(request):
    person = Person.objects.filter(user=request.user)[:1]
    if person :
        account_status = AccountStatus.objects.get(person=person)
        if not account_status :
            account_status = AccountStatus(person=person,status='I')
            account_status.save()
        vacations=[]
        last_demands_statuses=[]
        tasks=[]
        if account_status != "I" :
            vacations = Vacation.objects.filter(person=person)
            last_demands_statuses = DemandStatus.objects.filter(person=person).order_by('-encoding_date')[:5]
        context = {
            'vacations' : vacations,
            'last_demands_statuses' : last_demands_statuses,
            'person' : person,
            'tasks' : tasks
    }
    else :
        message = _('L''utilisateur ne correspond à aucune personne')
        error_messages=[message,]
        context = {'error_messages' : error_messages}
    return render(request, "home.html",context)

def ask_vacation(request,person_id):
    try :
        person = Person.objects.get(pk=person_id)
    except :
        pass
