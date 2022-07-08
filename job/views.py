from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Jop
from django.core.paginator import Paginator
from .form import ApplyForm, JobForm

# Create your views here.


def job_list(request):
    job_lists = Jop.objects.all()  # django query set
    paginator = Paginator(job_lists, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)


def job_details(request, slug):

    job_detail = Jop.objects.get(slug=slug)

    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job_detail
            my_form.save()
    else:
        form = ApplyForm()
    context = {'job': job_detail, 'form': form}
    return render(request, 'job/job_details.html', context)


def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    context = {'form': form}
    return render(request, 'job/add_job.html', context)
