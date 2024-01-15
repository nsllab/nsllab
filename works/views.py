from django.shortcuts import render
from .models import WeeklyReport
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import WeeklyReportForm

# Create your views here.


def weekly_reports(request):
    wr = WeeklyReport.objects.all().order_by('-fr_dt')
    context = {
        'reports': wr
    }
    return render(request, 'works/weeklyreport/reports.html', context)

class WeeklyReportCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url="/members/login"
    model = WeeklyReport
    form_class = WeeklyReportForm  # Replace with your actual form
    template_name = 'works/weeklyreport/create.html'  # Replace with your template name
    success_url = reverse_lazy('publications:conferences')  # Replace with your success URL
    success_message =  "Report added successfully"

    def form_valid(self, form):
        form.instance.writer = self.request.user  # Set the writer to the current user
        return super().form_valid(form)

class WeeklyReportDetailView(DetailView):
    model = WeeklyReport
    template_name = 'works/weeklyreport/details.html'
    context_object_name = 'report'