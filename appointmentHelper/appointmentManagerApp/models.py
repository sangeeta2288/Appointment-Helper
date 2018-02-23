from django.db import models


class Appointment(models.Model):
    description_text = models.CharField(max_length=200)
    appointment_date_time = models.DateTimeField('appointment date time')

    def __str__(self):
        return self.description_text+':'+str(self.appointment_date_time)