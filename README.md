# Appointment-Helper
Helps to add/edit appointments.
Front end is created using HTML, Bootstrap and jQuery.

    - HTML for simple rendering
    - Bootstrap for buttons and table
    - jquery for scripting and AJAX calls
    - All the above dependencies are loaded on the fly in index.html directly from cdn sites

Backend is using below technologies:

    - Django - 2.0.2 for hosting server and html templates
        - Python - 3.4.3
    - SQLite for data storage

Server can be run by below command:

    - python manage.py runserver

Features:

    - On the landing page, user gets option to add new appointment or search existing.
    - On blank search, user sees all his appointments
    - If a text is entered in search box, appointments will be filtered based on description match
    - On New , User will be able to add new appointment with description , date and time
    - On Add, page redirects to homepage saving the appointment details
    - There is a duplicate check, i.e., user is not allowed to add two appointments with same description

Open this in browser: http://localhost:8000/myAppointment/