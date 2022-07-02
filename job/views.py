from django.shortcuts import render
from .models import Jop
from django.core.paginator import Paginator


# Create your views here.


def job_list(request):
    job_lists = Jop.objects.all()  # django query set
    paginator = Paginator(job_lists, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)


def job_details(request, id):
    job_detail = Jop.objects.get(id=id)
    context = {'job': job_detail}
    return render(request, 'job/job_details.html', context)
