from django.shortcuts import render, get_object_or_404, redirect
from .models import Journal, Conference
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import JournalForm, JournalUpdateForm, ConferenceForm, ConferenceUpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DetailView
from .choices import PAPER_STATUS, PAPER_TYPE
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def journals(request):
    # query = request.GET.get('q')
    # print(f"QUery ########### {query}")
    journals = Journal.objects.order_by('-write_date')
    search = request.GET
    
    if 'title' in search:
        title = search['title']
        if title:
            journals = journals.filter(title__icontains=title)

    if 'year' in search:
        year = search['year']
        if year:
            journals = journals.filter(write_date__icontains=year)


    if 'journal_type' in search:
        journal_type = search['journal_type']
        if journal_type:
            journals = journals.filter(journal_type__iexact=journal_type)

    if 'status' in search:
        status = search['status']
        if status:
            journals = journals.filter(status__iexact=status)

    # if query:
    #     journals = journals.filter(
    #         Q(title__icontains=query) | Q(write_date__icontains=query)
    #     )

    context = {
        'journals': journals,
        'journal_type': PAPER_TYPE,
        'status': PAPER_STATUS,
    }
    return render(request, 'publications/journals/journals.html', context)

class JournalCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = "/members/login/"
    model = Journal
    form_class = JournalForm  # Replace with your actual form
    template_name = 'publications/journals/create.html'  # Replace with your template name
    success_url = reverse_lazy('publications:journals')  # Replace with your success URL
    success_message =  "%(journal_name)s created successfully"

    def form_valid(self, form):
        form.instance.writer = self.request.user  # Set the writer to the current user
        return super().form_valid(form)

@login_required(login_url="/members/login")
def journal_update(request, pk):
    journal = get_object_or_404(Journal, pk=pk)

    if request.method == 'POST':
        form = JournalUpdateForm(request.POST, request.FILES, instance=journal)
        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Update Successful')
            return redirect('publications:journals')
    else:
        form = JournalUpdateForm(instance=journal)

    context = {
        'form': form,
    }

    return render(request, 'publications/journals/update.html', context)


class JournalDetailView(DetailView):
    model = Journal
    template_name = 'publications/journals/journal_details.html'
    context_object_name = 'journal'


def conferences(request):
    conferences = Conference.objects.order_by('-write_date')
    search = request.GET
    
    if 'title' in search:
        title = search['title']
        if title:
            conferences = conferences.filter(title__icontains=title)

    if 'year' in search:
        year = search['year']
        if year:
            conferences = conferences.filter(write_date__icontains=year)


    if 'journal_type' in search:
        conference_type = search['conference_type']
        if conference_type:
            conferences = conferences.filter(conference_type__iexact=conference_type)

    if 'status' in search:
        status = search['status']
        if status:
            conferences = conferences.filter(status__iexact=status)

    context = {
        'conferences': conferences,
        'journal_type': PAPER_TYPE,
        'status': PAPER_STATUS,
    }
    return render(request, 'publications/conferences/conferences.html', context)



class ConferenceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url="/members/login"
    model = Conference
    form_class = ConferenceForm  # Replace with your actual form
    template_name = 'publications/conferences/create.html'  # Replace with your template name
    success_url = reverse_lazy('publications:conferences')  # Replace with your success URL
    success_message =  "Conference added successfully"

    def form_valid(self, form):
        form.instance.writer = self.request.user  # Set the writer to the current user
        return super().form_valid(form)


class ConferenceDetailView(DetailView):
    model = Conference
    template_name = 'publications/conferences/conference_details.html'
    context_object_name = 'conference'

@login_required(login_url="/members/login")
def conference_update(request, pk):
    conference = get_object_or_404(Conference, pk=pk)

    if request.method == 'POST':
        form = ConferenceUpdateForm(request.POST, request.FILES, instance=conference)
        
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Update Successful')
            return redirect('publications:conferences')
    else:
        form = ConferenceUpdateForm(instance=conference)

    context = {
        'form': form,
    }

    return render(request, 'publications/conferences/update.html', context)
