from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate part
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in! :D")
            return redirect('home')
        else:
            messages.success(request, "There was an error, pls try again umu")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

    

#login_user/logout_user is used because "login/logout" is already a function, up there at the import thing.
def logout_user(request):
    pass 


#notes
#if person is logging in, they are POST -ing, otherwish they are GET -ing. the request. it's like a bounty in an adveture guild.