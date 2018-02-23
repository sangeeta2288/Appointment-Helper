from django.http import HttpResponse
from django.shortcuts import render_to_response
from appointmentManagerApp.models import Appointment
from django.core import serializers

def index(request):
    return render_to_response('index.html')

def getAppointment(request, search_string):
    result = Appointment.objects.get(description_text=search_string)
    serialized_obj = serializers.serialize('json', [result, ])
    return HttpResponse(serialized_obj)