from django.template import loader
from django.http import HttpResponse
from CampusConnectApp.models import Contact
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib import messages


def profile(request):
    email = request.user.email
    current_user = get_object_or_404(User, email=email)
    print(current_user)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Added Successfully!')
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
