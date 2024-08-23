from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.urls import reverse_lazy


# Create your views here.

class DetailsView(TemplateView):
    template_name = 'Dating/details.html'
    success_url = reverse_lazy('new_app:job_status')

class JobStatusView(TemplateView):
    template_name = 'Dating/job_status.html'
    success_url = reverse_lazy('new_app:job_details')

class JobDetailsView(TemplateView):
    template_name = 'Dating/job_details.html'



