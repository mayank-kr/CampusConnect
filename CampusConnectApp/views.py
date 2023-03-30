from django.template import loader
from django.http import HttpResponse
from .models import Contact, Users, Sell
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserForm, SellForm

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
    if request.method == 'POST':
        form = SellForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/buy')
    else:
        form = SellForm()
    return render(request, 'sell.html', {'form': form})
