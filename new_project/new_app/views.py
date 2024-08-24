from typing import Any

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView

from.forms import *
from .forms import RegisterForm, EmployerForm
from .models import   User, Interest


# Create your views here.

class DetailsView(FormView):
    form_class = RegisterForm
    template_name = 'Dating/details.html'
    success_url = reverse_lazy('new_app:job_status')



    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs.update({
                'instance': self.request.user,
                'data': self.request.POST or None,
            })
        else:
            kwargs.update({
                'data': self.request.POST or None,
            })
        return kwargs

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.save()
        return super().form_valid(form)


class JobStatusView(FormView):
    template_name = 'Dating/job_status.html'
    success_url = reverse_lazy('new_app:job_details')

class JobDetailsView(FormView):
    template_name = 'Dating/job_details.html'
    form_class = EmployerForm

    def get_form_kwargs(self):
        return {'instance': self.request.user,
                'data': self.request.POST}

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)



