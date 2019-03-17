from django.shortcuts import render
from .models import Receiver
from django.http import HttpResponse

# Create your views here.
def index ( request ):
    """
    Shows a list with every possible receptor, so that the user can see active reminders
    """

    receiver=Receiver.objects.all()
    context=dict()
    return render(request, 'reminderapp/index.html', context)
#Fin de función index