from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'migrations/hello.html' )
def password(request):
    charaster =list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charaster.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        charaster.extend(list('!"#$ % &()*+,-./:;<=>?@[\]^_`{|}~'))
    if request.GET.get('numbers'):
        charaster.extend(list('1234567890'))
    length = int(request.GET.get('length',11))
    thepassword = ""
    for x in range(length):
        thepassword += random.choice(charaster)
    return render(request, 'migrations/password.html', {'password': thepassword})
def aboutme(request):
    return render(request, 'migrations/aboutme.html' )