from django.template import loader
from django.http import HttpResponse
from.models import auth

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())
def signin(request):
    uname = auth.objects.all().values()
    context ={
        'uname':uname
    }
    template = loader.get_template('signin.html')
    return HttpResponse(template.render(context,request))
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({},request))
def signout(request):
    pass