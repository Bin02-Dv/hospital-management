from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.urls import reverse
from .models import PatientR, Room
from itertools import chain

# Create your views here.

@login_required(login_url='login')
def index(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'index.html', {'user': user})

def signUp(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Exist....')
                return redirect('signUp')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Exist...')
                return redirect('signUp')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password and Confirmpassword missed match...')
            return redirect('signUp')
    else:
        return render(request, 'signUp.html')


def login(request):

    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Inverlid Credentials....')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def patient_view(request):

    rooms = Room.objects.all()
    patients = PatientR.objects.all()

    return render(request, 'patient-view.html', {'rooms':rooms, 'patients':patients})

@login_required(login_url='login')
def room_list(request):
    return render(request, 'room-list.html')

@login_required(login_url='login')
def add_patient(request):

    if request.method == 'POST':
        full_name = request.POST['full_name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        marital = request.POST['marital']
        lga = request.POST['lga']
        addrss = request.POST['address']
        state = request.POST['state']
        room = request.POST['room']
        apparatus = request.POST['apparatus']
        code = request.POST['code']

        if len(full_name) != 0:

            if PatientR.objects.filter(code=code).exists():
                messages.info(request, 'code already exist... please rerun the code again..')
                return redirect('patient-view')
            else:
                new_patient = PatientR.objects.create(full_name=full_name, dob=dob, gender=gender,marital=marital, lga=lga, addrss=addrss, state=state,room=room, apparatus=apparatus, code=code)
                new_patient.save()
                return redirect('patient-view')
    else:
        return redirect('add-patient')

@login_required(login_url='login')
def update(request, id):
  patient = PatientR.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'patient': patient,
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def updaterecord(request, id):
    full_name = request.POST['full_name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    marital = request.POST['marital']
    lga = request.POST['lga']
    addrss = request.POST['address']
    state = request.POST['state']
    room = request.POST['room']
    apparatus = request.POST['apparatus']

    patient = PatientR.objects.get(id=id)
    patient.full_name = full_name
    patient.dob = dob
    patient.gender = gender
    patient.marital = marital
    patient.lga = lga
    patient.addrss = addrss
    patient.state = state
    patient.room = room
    patient.apparatus = apparatus
    patient.save()
    return HttpResponseRedirect(reverse('patient-view'))

@login_required(login_url='login')
def p_details(request, pk):
    p = PatientR.objects.get(id=pk)
    return render(request, 'p_details.html', {'p': p})


@login_required(login_url='login')
def search(request):
    if request.method == 'POST':
        code = request.POST['code']
        patient = PatientR.objects.filter(code__icontains=code)

        patient_profile = []
        patient_profile_list = []

        for patients in patient:
            patient_profile.append(patients.id)

        for ids in patient_profile:
            profile_list = PatientR.objects.filter(id=ids)
            patient_profile_list.append(profile_list)
        patient_profile_list = list(chain(*patient_profile_list))
    return render(request, 'search.html', {'patient_profile_list': patient_profile_list})

def delete(request, id):
    patient = PatientR.objects.get(id=id)
    patient.delete()
    return HttpResponseRedirect(reverse('patient-view'))