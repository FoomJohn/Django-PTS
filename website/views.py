from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, ScoreForm
from .models import Record, ScoreEverything


def home(request):

    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate part
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome! You are logged in! :D")
            return redirect('home')
        else:
            messages.success(request, "There was an error, pls try again umu")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

    
def logout_user(request):
    logout(request)
    messages.success(request, "aight, you logged out, bai!!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #autheticate, kinda like autologin after register
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You is now the registered hehee~")
            return redirect('home')

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})
    

def candidate_record(request, pk):
    if request.user.is_authenticated:
        #look up the record pk
        candidate_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'candidate_record': candidate_record})
    else:
        messages.success(request, "You must be logged in to do that")
        return redirect('home')
        

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to do that")
        return redirect('home')
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to add stuff")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to add stuff")
        return redirect('home')
#notes
#if person is logging in, they are POST -ing, otherwish they are GET -ing. the request. it's like a bounty in an adveture guild.
    

"""
def score_candidate(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = ScoreForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated")
            #return redirect('home')
        return render(request, 'score_candidate.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to add stuff")
        return redirect('home')
"""

def score_candidate(request, pk):
    current_record = get_object_or_404(Record, id=pk)
    judge = request.user

    # Check if the judge has already scored this candidate
    score_exists = ScoreEverything.objects.filter(candidate=current_record, judge=judge).exists()

    if request.method == "POST":
        form = ScoreForm(request.POST, request.FILES)
        if form.is_valid() and not score_exists:
            instance = form.save(commit=False)
            instance.judge = request.user
            instance.candidate = current_record
            instance.save()
            messages.success(request, "Judged")
            return redirect('home')
    else:
        form = ScoreForm()

    return render(request, 'score_candidate.html', {'form': form, 'current_record': current_record, 'score_exists': score_exists})

































def tabulation(request):
    
    scoreeverythings = ScoreEverything.objects.all()

    if request.user.is_authenticated:
        return render(request, 'tabulation.html', {'scoreeverythings':scoreeverythings})
    else:
        messages.success(request, "noo")
        return redirect('home')
    
def tabulation_production_number(request):
    
    scoreeverythings = ScoreEverything.objects.all()

    if request.user.is_authenticated:
        return render(request, 'tabulation_production_number.html', {'scoreeverythings':scoreeverythings})
    else:
        messages.success(request, "noo")
        return redirect('home')      

def tabulation_swimsuit(request):
    
    scoreeverythings = ScoreEverything.objects.all()

    if request.user.is_authenticated:
        return render(request, 'tabulation_swimsuit.html', {'scoreeverythings':scoreeverythings})
    else:
        messages.success(request, "noo")
        return redirect('home')   
    
def tabulation_evening_gown(request):
    
    scoreeverythings = ScoreEverything.objects.all()

    if request.user.is_authenticated:
        return render(request, 'tabulation_evening_gown.html', {'scoreeverythings':scoreeverythings})
    else:
        messages.success(request, "noo")
        return redirect('home')   
    
def tabulation_q_and_a(request):
    
    scoreeverythings = ScoreEverything.objects.all()

    if request.user.is_authenticated:
        return render(request, 'tabulation_q_and_a.html', {'scoreeverythings':scoreeverythings})
    else:
        messages.success(request, "noo")
        return redirect('home')   