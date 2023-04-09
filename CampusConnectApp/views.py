from django.template import loader
from django.http import HttpResponse
from .models import Contact, Users, Sell, Lost, Found, CabSharing, Mess, Restaurants
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, SellForm, LostForm, FoundForm, CabSharingForm
from django.utils import timezone
import datetime

# from django.contrib.auth.views import LoginView


# class GoogleLoginView(LoginView):
#     template_name = 'google_login.html'


def profile(request):
    email = request.user.email
    current_user = User.objects.get(email=email)
    print(current_user.email)

    try:
        if (Users.objects.get(email=email)) is not None:
            return redirect('/')

    except:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                print("Profile Added Successfully!")
                return redirect('/')
            else:
                print("Error Adding Profile")
        else:
            form = UserForm()
        return render(request, 'profile.html', {'form': form})


def emergency(request):
    getdata = Contact.objects.all().filter(type='Emergency')
    template = loader.get_template('emergency.html')
    context = {
        'contacts': getdata
    }
    return HttpResponse(template.render(context, request))


def administration(request):
    getdata = Contact.objects.all().filter(type='Administration')
    template = loader.get_template('administration.html')
    context = {
        'contacts': getdata
    }
    return HttpResponse(template.render(context, request))


def faculty(request):
    getdata = Contact.objects.all().filter(type='Faculty')
    template = loader.get_template('faculty.html')
    context = {
        'contacts': getdata
    }
    return HttpResponse(template.render(context, request))


def buy(request):
    getdata = Sell.objects.all()
    template = loader.get_template('buy.html')
    context = {
        'data': getdata
    }
    return HttpResponse(template.render(context, request))


def sell(request):
    email = request.user.email
    current_user = Users.objects.get(email=email)
    if request.method == 'POST':
        form = SellForm(request.POST, initial={'roll': current_user})
        if form.is_valid():
            form.save()
            return redirect('/buy')
    else:
        form = SellForm(initial={'roll': current_user})
    return render(request, 'sell.html', {'form': form})


def lost(request):
    getdata = Lost.objects.all()
    template = loader.get_template('lost.html')
    context = {
        'data': getdata
    }
    return HttpResponse(template.render(context, request))


def found(request):
    getdata = Found.objects.all()
    template = loader.get_template('found.html')
    context = {
        'data': getdata
    }
    return HttpResponse(template.render(context, request))


def lostform(request):
    email = request.user.email
    current_user = Users.objects.get(email=email)
    if request.method == 'POST':
        form = LostForm(request.POST, request.FILES,
                        initial={'roll': current_user})
        if form.is_valid():
            form.save()
            return redirect('/lostfound/lost')
        else:
            print("Error in lost form submission")
    else:
        form = LostForm(initial={'roll': current_user})
    return render(request, 'lostform.html', {'form': form})


def foundform(request):
    email = request.user.email
    current_user = Users.objects.get(email=email)
    if request.method == 'POST':
        form = FoundForm(request.POST, request.FILES,
                         initial={'roll': current_user})
        if form.is_valid():
            form.save()
            return redirect('/lostfound/found')
        else:
            print("Error in lost form submission")
    else:
        form = LostForm(initial={'roll': current_user})
    return render(request, 'foundform.html', {'form': form})


def cabsharing(request):
    getdata = CabSharing.objects.all()
    template = loader.get_template('cabsharing.html')
    context = {
        'data': getdata
    }
    return HttpResponse(template.render(context, request))


def cabsharingform(request):
    email = request.user.email
    current_user = Users.objects.get(email=email)
    error_msg = ""
    if request.method == 'POST':
        form = CabSharingForm(request.POST, initial={'roll': current_user})
        if form.is_valid():
            form_time = form.cleaned_data['time']
            if form_time > timezone.now():
                form.save()
                return redirect('/cabsharing')
            else:
                error_msg = 'Invalid time, time must be in future'
    else:
        form = CabSharingForm(initial={'roll': current_user})
    return render(request, 'cabsharingform.html', {'form': form, 'error': error_msg})


def mess(request):
    now = datetime.datetime.now()
    getdata = Mess.objects.all().filter(day=(now.strftime("%A")))
    template = loader.get_template('mess.html')
    context = {
        'day': now.strftime("%A"),
        'data': getdata
    }
    return HttpResponse(template.render(context, request))


def restaurants(request):
    getdata = Restaurants.objects.all().order_by('distance')
    template = loader.get_template('restaurants.html')
    context = {
        'data': getdata
    }
    return HttpResponse(template.render(context, request))


def timetable(request):
    email = request.user.email
    current_user = Users.objects.get(email=email)
    user_year = current_user.batch
    print(user_year)
    template = loader.get_template('timetable.html')
    return HttpResponse(template.render({'year': user_year}, request))
