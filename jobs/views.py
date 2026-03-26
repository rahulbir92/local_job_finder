from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all().order_by('-posted_date')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})
