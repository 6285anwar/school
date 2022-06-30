from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import *


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['Adm_id'] = user.id
            return redirect('dashboard')

    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    teach = teacher.objects.all()
    return render(request, 'dashboard.html', {'teach': teach})


def addteacher(request):

    return render(request, 'addteacher.html')


def typeinput(request):
    if request.method == 'POST':
        t = teacher()
        t.firstname = request.POST['fn']
        t.lastname = request.POST['ln']
        t.email = request.POST['e']
        t.phone = request.POST['pn']
        t.subjects = request.POST['s']
        t.room = request.POST['rn']
        t.photo = request.FILES['pic']
        t.save()
        return redirect('dashboard')
    return render(request, 'addteacher.html')


def profile(request, id):
    t = teacher.objects.get(id=id)

    return render(request, 'profile.html', {'t': t})


def upload_csv(request):

    if request.method == "POST":
        csv_file = request.FILES["csvfile"]

        if not csv_file.name.endswith('.csv'):
            messages.warning(request, 'The wrong file type was uploaded')
            return HttpResponseRedirect(request.path_info)

        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")

        for x in csv_data:
            fields = x.split(",")
            created = teacher.objects.update_or_create(
                firstname=fields[0],
                lastname=fields[1],
                photo=fields[2],
                email=fields[3],
                phone=fields[4],
                room=fields[5],
                subject=fields[6],

            )
            return redirect('dashboard')
  
