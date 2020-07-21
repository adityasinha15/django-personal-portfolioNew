from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Image, Certification, Profile, Contact
import datetime

# Create your views here.
def home(request):
    projects = Project.objects.all()
    certificates = Certification.objects.all()
    profile = Profile.objects.get(fname='Aditya')
    dob = str(profile.dob)
    year = dob[0:4]
    now_date = str(datetime.datetime.now())
    current_year = now_date[0:4]
    age = int(current_year) - int(year) - 1
    
    resume = profile.resume
    return render(request, 'portfolio/index.html', {'projects':projects, 'certificates':certificates, 'age':age, 'resume':resume})

def project_detail(request, pid):
    project = Project.objects.get(id=pid)
    images = Image.objects.get(project=project)
    tech = project.technologies
    tech_list = tech.split(',')
    technology = []
    for item in tech_list:
        technology.append(item.capitalize())

    print(images.img1)
    
    
    return render(request, 'portfolio/portfolio-1.html', {'project':project, 'images':images, 'tech':technology})


def contact(request):
    if request.method == 'GET':
        return render(request, 'portfolio/index.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        temp = Contact(name=name, email=email, subject=subject, message=message)
        temp.save()
        temp.commit()
        print(temp)
        return render(request, 'portfolio/index.html')
