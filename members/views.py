# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login
from .forms import MemberCreationForm, LoginForm
from django.contrib import messages
from .models import Bio
from django.views.generic import CreateView, UpdateView, DetailView

def register_user(request):
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)  # Log in the user after registration
            messages.add_message(request, messages.SUCCESS, f'Thanks for registering {user.username}. Contact admin to activate your account')
            return redirect('members:login')  # Redirect to the home page or any other page you want
    else:
        form = MemberCreationForm()

    return render(request, 'members/registration.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f'Welcome back {user.username}')
                return redirect('publications:journals')  # Redirect to the home page or any other page you want
            else:
                messages.add_message(request, messages.ERROR, 'Invalid Credentials. Login Unsuccessful. Contact Admin')
    else:
        form = LoginForm()

    return render(request, 'members/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, f'See you soon {request.user.username}')
    return redirect('publications:journals')

def professors_list(request):

    bio = Bio.objects.filter(position=1)
    context = {
        'bios': bio,
        'total': len(bio)
        }
    return render(request, 'members/professors.html', context)

def post_docs_list(request):

    bio = Bio.objects.filter(position=2)
    context = {
        'bios': bio,
        'total': len(bio)
        }
    return render(request, 'members/post_docs.html', context)


class PostDoctDetailView(DetailView):
    model = Bio
    template_name = 'members/post_doc_detail.html'
    context_object_name = 'post_doc'