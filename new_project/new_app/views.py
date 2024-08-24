from typing import Any

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,ListView,FormView

from.forms import *
from .forms import RegisterForm, EmployerForm
from .models import   User, Interest


# Create your views here.

class DetailsView(TemplateView):
    form_class = RegisterForm
    template_name = 'dating/details.html'
    success_url = reverse_lazy('Dating_app:job_status')

    def get_form_kwargs(self):
        return {'instance': self.request.user,
                'data': self.request.POST}

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class JobStatusView(TemplateView):
    template_name = 'Dating/job_status.html'
    success_url = reverse_lazy('new_app:job_details')

class JobDetailsView(TemplateView):
    template_name = 'dating/job_details.html'
    form_class = EmployerForm

    def get_form_kwargs(self):
        return {'instance': self.request.user,
                'data': self.request.POST}

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)



