from django.db import connection, transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, ScoreForm
from .models import Candidate, ScoreEverything


def home(request):

    candidates = Candidate.objects.all()
    
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
        return render(request, 'home.html', {'candidates':candidates})

    
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
        current_record = get_object_or_404(Candidate, id=pk)
        candidate_record = Candidate.objects.get(id=pk)
        return render(request, 'record.html', {'candidate_record': candidate_record, 'current_record': current_record})
    else:
        messages.success(request, "You must be logged in to do that")
        return redirect('home')
        

def delete_candidate(request, pk):
    if request.user.is_authenticated:
        delete_it = Candidate.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Candidate Deleted")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to do that")
        return redirect('home')
    
"""
def add_candidate(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to add stuff")
        return redirect('home')
"""

def add_candidate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddRecordForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        else:
            form = AddRecordForm()
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to add stuff")
        return redirect('home')


def update_candidate(request, pk):
    if request.user.is_authenticated:
        candidate_record = get_object_or_404(Candidate, id=pk)
        current_record = Candidate.objects.get(id=pk)
        if request.method == "POST":
            form = AddRecordForm(request.POST or None, request.FILES, instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Updated")
                return redirect('home')
        else:
            form = AddRecordForm()
        return render(request, 'update_record.html', {'form':form, 'candidate_record': candidate_record, 'current_record': current_record})
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
    current_record = get_object_or_404(Candidate, id=pk)
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

def reset_auto_increment(table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;")


def delete_all_candidate(request):
    if request.user.is_authenticated:
        # Step 1: Delete all candidate objects
        Candidate.objects.all().delete()

        # Step 2: Reset the primary key sequence
        try:
            # Reset auto-increment for website_candidate table
            reset_auto_increment("website_candidate")


            # Commit the transaction
            transaction.commit()

        except Exception as e:
            # Rollback the transaction if any error occurs
            transaction.rollback()
            raise e
        messages.success(request, "All Candidates Removed")
        return redirect('home')  

    else:
        messages.success(request, "You must be logged in to add stuff")
        return redirect('home')
    
    



























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