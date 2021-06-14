from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee, MobileNumber, Device
from .forms import MobileNumberForm, LoginForm
from .filters import NumbersFilter, DevicesFilter
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')  # HttpResponse('Uwierzytelnienie zakończyło się sukcesem.')
                else:
                    return HttpResponse('Konto jest zablokowane.')
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniające.')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def devices_list(request):
    devices = Device.objects.all()
    my_filter2 = DevicesFilter(request.GET, queryset=devices)
    devices = my_filter2.qs
    return render(request, 'devices_list.html', {'devices': devices, 'filter': my_filter2})


def mobile_numbers(request):
    numbers = MobileNumber.objects.all()
    users = Employee.objects.all()
    result = MobileNumber.objects.count()
    my_filter = NumbersFilter(request.GET, queryset=numbers)
    numbers = my_filter.qs
    return render(request, 'mobile_numbers.html', {'numbers': numbers, 'result': result, 'users': users,
                                                   'my_filter': my_filter})


def mobile_number_edit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MobileNumberForm()
        else:
            number = MobileNumber.objects.get(pk=id)
            form = MobileNumberForm(instance=number)
        return render(request, "mobile_number_edit.html", {'form': form})
    else:
        if id == 0:
            form = MobileNumberForm(request.POST)
        else:
            number = MobileNumber.objects.get(pk=id)
            form = MobileNumberForm(request.POST, instance=number)
        if form.is_valid():
            form.save()
        return redirect("/mobile_numbers")


def mobile_number_add(request):
    if request.method == "GET":
        form = MobileNumberForm()
        return render(request, "mobile_number_edit.html", {'form': form})
    else:
        form = MobileNumberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/mobile_numbers")


def mobile_number_delete(request, id):
    number = MobileNumber.objects.get(pk=id)
    if request.method == "GET":
        return render(request, "number_delete.html", {'number': number})
    else:
        number.delete()
    return redirect("/mobile_numbers")


def chart(request):
    labels = []
    queryset = Device.objects.all()
    queryset1 = MobileNumber.objects.all()
    labels1 = []

    for device in queryset:
        labels.append(device.model)
    a = dict((device, labels.count(device)) for device in labels)
    data = list(a.values())
    labels = list(a.keys())

    for number in queryset1:
        labels1.append(number.tariff)

    return render(request, 'chart.html', {
        'labels': labels,
        'data': data,
        'labels1': labels1,
        'data1': data
    })
