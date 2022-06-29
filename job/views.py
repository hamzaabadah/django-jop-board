from django.shortcuts import render
from .models import Jop


# Create your views here.


def job_list(request):
    job_lists = Jop.objects.all()  # django query set
    print(job_lists)  # template name
    context = {'jobs': job_lists}
    return render(request, 'job/job_list.html', context)


def job_details(request, id):
    job_detail = Jop.objects.get(id=id)
    context = {'job': job_detail}
    return render(request, 'job/job_details.html', context)
