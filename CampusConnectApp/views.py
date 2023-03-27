from django.template import loader
from django.http import HttpResponse
from CampusConnectApp.models import Contact


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
