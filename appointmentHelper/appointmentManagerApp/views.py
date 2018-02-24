from django.http import HttpResponse
from django.shortcuts import render_to_response
from appointmentManagerApp.models import Appointment
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime
from django.shortcuts import redirect

def index(request):
    date = request.GET.get('date-input', '')
    time = request.GET.get('time-input', '')
    description = request.GET.get('desc-input', '')
    #if all fields are not empty the save the details to db
    if (date != '' and time != '' and description != ''):
        parseAndSaveToDB(date, time, description)
        return redirect('/myAppointment/')
    return render_to_response('index.html')

def getAppointment(request, search_string=''):
    # if search_string is empty return all
    if (search_string == '%empty%'):
        result = Appointment.objects.all()
    else:
        result = Appointment.objects.filter(description_text__contains=search_string)
    return JsonResponse(serializers.serialize('json', result), safe=False)

def parseAndSaveToDB(date, time, description):
    #if already exists, return
    result = Appointment.objects.filter(description_text__contains=description)
    if len(result):
        return
    parsed_datetime = datetime.strptime(date+ ' ' +time, "%Y-%m-%d %H:%M")
    appointment_to_save = Appointment(description_text = description, appointment_date_time = parsed_datetime)
    appointment_to_save.save()