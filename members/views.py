# views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate, login
from .forms import MemberCreationForm, LoginForm, MemberUpdateForm
from django.contrib import messages
from .models import Bio, Member
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class MemberUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Member
    form_class = MemberUpdateForm
    template_name = 'members/update_profile.html'  # Your template for updating profile
    success_url = reverse_lazy('pages:index')  # Redirect to the user's profile page
    success_message = "Profile successfully updated."

    def get_object(self, queryset=None):
        return self.request.user  # Get the currently logged-in user

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        existing_user = Member.objects.exclude(pk=self.request.user.pk).filter(username=username).exists()
        
        if existing_user:
            messages.add_message(self.request, messages.ERROR, 'Username already exists. Please choose a different username.')
            return self.form_invalid(form)
        
        return super().form_valid(form)

class MemberChangePasswordView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'members/change_password.html'  # Your template for changing password
    success_url = reverse_lazy('pages:index')  # Redirect to the user's profile page
    success_message = "Your password was successfully updated."

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

# def professors_list(request):

#     bio = Bio.objects.filter(position=1)
#     context = {
#         'bios': bio,
#         'total': len(bio)
#         }
#     return render(request, 'members/professors.html', context)

class ProfessorsListView(ListView):
    model = Bio
    template_name = 'members/professors.html'
    context_object_name = 'bios'

    def get_queryset(self):
        return Bio.objects.filter(position=1).order_by('display_order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.get_queryset().count()
        return context


class PostDocsListView(ListView):
    model = Bio
    template_name = 'members/post_docs.html'
    context_object_name = 'bios'

    def get_queryset(self):
        return Bio.objects.filter(position=2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.get_queryset().count()
        return context


class FullTimeListView(ListView):
    model = Bio
    template_name = 'members/full_time.html'
    context_object_name = 'bios'

    def get_queryset(self):
        return Bio.objects.filter(position=3).order_by('display_order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = self.get_queryset().count()
        return context


class PostDoctDetailView(DetailView):
    model = Bio
    template_name = 'members/post_doc_detail.html'
    context_object_name = 'post_doc'

class FullTimeDetailView(DetailView):
    model = Bio
    template_name = 'members/full_time_detail.html'
    context_object_name = 'full_time'